#!/usr/bin/env python3
"""Static integrity checks for CR Knowledge Base (no network required)."""
from __future__ import annotations

from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlparse

import yaml

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []
SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
LEVELS = ("R0", "R1", "R2", "R3", "R4")
EVIDENCE = {"unknown", "author-documented", "source-inspected", "reproduced"}
INTEGRATION = {"unverified", "tested", "maintained"}


def bad(where: str, what: str) -> None:
    ERRORS.append(f"{where}: {what}")


def read_yaml(path: str, field: str) -> list[dict]:
    try:
        data = yaml.safe_load((ROOT / path).read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        bad(path, f"cannot parse: {exc}")
        return []
    if not isinstance(data, dict) or not isinstance(data.get(field), list):
        bad(path, f"expected a top-level '{field}' list")
        return []
    rows = data[field]
    if not all(isinstance(x, dict) for x in rows):
        bad(path, f"every entry of '{field}' must be an object")
        return []
    return rows


def index(rows: list[dict], collection: str) -> dict[str, dict]:
    result = {}
    for row in rows:
        ident = row.get("id")
        if not isinstance(ident, str) or not SLUG.fullmatch(ident):
            bad(collection, f"invalid id {ident!r}")
            continue
        if ident in result:
            bad(collection, f"duplicate id {ident}")
        result[ident] = row
        path = row.get("path")
        if not isinstance(path, str) or not (ROOT / path).is_file():
            bad(collection, f"{ident}: missing markdown path {path!r}")
    return result


def frontmatter(path: str, expected_id: str, expected_type: str) -> dict:
    file = ROOT / path
    if not file.is_file():
        return {}
    text = file.read_text(encoding="utf-8")
    parts = text.split("---\n", 2)
    if not text.startswith("---\n") or len(parts) < 3:
        bad(path, "missing YAML front matter")
        return {}
    try:
        meta = yaml.safe_load(parts[1])
    except yaml.YAMLError as exc:
        bad(path, f"invalid front matter: {exc}")
        return {}
    if not isinstance(meta, dict):
        bad(path, "front matter must be an object")
        return {}
    if meta.get("id") != expected_id or meta.get("type") != expected_type:
        bad(path, f"expected id={expected_id} and type={expected_type}")
    return meta


projects = index(read_yaml("registry/projects.yaml", "projects"), "projects")
topics = index(read_yaml("registry/topics.yaml", "topics"), "topics")
caps = index(read_yaml("registry/capabilities.yaml", "capabilities"), "capabilities")
impls = read_yaml("registry/implementations.yaml", "implementations")
rels = read_yaml("registry/relationships.yaml", "relationships")

for pid, row in projects.items():
    path = row.get("path", "")
    meta = frontmatter(path, pid, "project")
    if not str(row.get("repository", "")).startswith("https://github.com/"):
        bad(pid, "missing GitHub repository")
    if row.get("verification") not in EVIDENCE:
        bad(pid, f"invalid verification {row.get('verification')}")
    if meta:
        for key in ("repository", "verification", "license"):
            if meta.get(key) != row.get(key):
                bad(pid, f"project metadata differs from registry: {key}")
        if set(meta.get("topics", [])) != set(row.get("topics", [])):
            bad(pid, "topic references differ from registry")
    for tid in row.get("topics", []):
        if tid not in topics:
            bad(pid, f"unknown topic {tid}")
        elif pid not in topics[tid].get("projects", []):
            bad(pid, f"topic {tid} missing reverse relation")

for tid, row in topics.items():
    meta = frontmatter(row.get("path", ""), tid, "topic")
    if meta and set(meta.get("projects", [])) != set(row.get("projects", [])):
        bad(tid, "project references differ from topic registry")
    for pid in row.get("projects", []):
        if pid not in projects:
            bad(tid, f"unknown project {pid}")
        elif tid not in projects[pid].get("topics", []):
            bad(tid, f"project {pid} missing reverse relation")

for cid, row in caps.items():
    meta = frontmatter(row.get("path", ""), cid, "capability")
    if meta:
        for key in ("lifecycle", "standardization"):
            if meta.get(key) != row.get(key):
                bad(cid, f"capability metadata differs: {key}")

seen_pairs: set[tuple[str, str]] = set()
seen_impl_ids: set[str] = set()
for rec in impls:
    cid, pid = rec.get("capability"), rec.get("project")
    where = f"implementation {rec.get('id', '?')}"
    if cid not in caps or pid not in projects:
        bad(where, f"unknown endpoints {cid!r} / {pid!r}")
        continue
    pair = (cid, pid)
    if pair in seen_pairs:
        bad(where, "duplicate capability-project association")
    seen_pairs.add(pair)
    ident = f"{cid}--{pid}"
    if rec.get("id") != ident or ident in seen_impl_ids:
        bad(where, f"expected unique implementation id {ident}")
    seen_impl_ids.add(ident)
    rank = rec.get("reuse_level")
    if rank not in LEVELS:
        bad(where, f"invalid reuse level {rank!r}")
    if rec.get("verification") not in EVIDENCE:
        bad(where, "invalid evidence level")
    if rec.get("integration") not in INTEGRATION:
        bad(where, "invalid integration state")
    if not isinstance(rec.get("evidence"), str) or not rec["evidence"].startswith("https://"):
        bad(where, "evidence must be a source URL")
    if not rec.get("claim") or not rec.get("limits"):
        bad(where, "claim and limits are required")
    if rank in ("R2", "R3", "R4") and rec.get("verification") not in ("source-inspected", "reproduced"):
        bad(where, "R2+ requires source inspection or independent reproduction")
    if rank in ("R3", "R4"):
        if rec.get("verification") != "reproduced":
            bad(where, "R3+ requires independent reproduction")
        if rec.get("integration") not in ("tested", "maintained"):
            bad(where, "R3+ requires tested integration")
        if projects[pid].get("license") in (None, "unknown"):
            bad(where, "R3+ cannot skip license verification")

for cid in caps:
    if not any(x[0] == cid for x in seen_pairs):
        bad(cid, "capability has no linked implementations")

for rec in rels:
    where = f"relationship {rec.get('from')} -> {rec.get('to')}"
    if rec.get("from") not in projects or rec.get("to") not in projects:
        bad(where, "unknown project endpoint")
    if not str(rec.get("evidence", "")).startswith("https://"):
        bad(where, "missing evidence URL")
    if not rec.get("type"):
        bad(where, "missing relationship type")

for file in ROOT.rglob("*.md"):
    relative = file.relative_to(ROOT).as_posix()
    text = file.read_text(encoding="utf-8")
    # Ignore fenced code snippets when looking for hyperlinks.
    text = re.sub(r"(?ms)^\s*`{3}.*?^\s*`{3}[^\n]*$", "", text)
    for raw in MARKDOWN_LINK.findall(text):
        href = raw.split(maxsplit=1)[0].strip("<>")
        parsed = urlparse(href)
        if not href or parsed.scheme or href.startswith(("#", "/")):
            continue
        path = unquote(parsed.path)
        dest = (file.parent / path).resolve()
        if not dest.is_relative_to(ROOT) or not dest.exists():
            bad(relative, f"broken relative link {href!r}")

for error in ERRORS:
    print("ERROR:", error)
print(f"Verified {len(projects)} projects, {len(topics)} research topics, "
      f"{len(caps)} capabilities, {len(impls)} implementations, "
      f"{len(rels)} relationships. {len(ERRORS)} issue(s).")
sys.exit(1 if ERRORS else 0)
