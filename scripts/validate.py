#!/usr/bin/env python3
"""Validate the project/topic registry and local cross-references."""
from pathlib import Path
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
errors = []

def load(path, key):
    data = yaml.safe_load((ROOT / path).read_text(encoding="utf-8"))
    if not isinstance(data, dict) or not isinstance(data.get(key), list):
        errors.append(f"{path}: expected list '{key}'")
        return []
    return data[key]

projects = load("registry/projects.yaml", "projects")
topics = load("registry/topics.yaml", "topics")
rels = load("registry/relationships.yaml", "relationships")

def indexed(rows, label):
    index = {}
    for row in rows:
        if not isinstance(row, dict) or not isinstance(row.get("id"), str):
            errors.append(f"{label}: entry missing string id")
            continue
        i = row["id"]
        if i in index:
            errors.append(f"{label}: duplicate id {i}")
        index[i] = row
        p = row.get("path")
        if not isinstance(p, str) or not (ROOT / p).is_file():
            errors.append(f"{label}/{i}: missing file {p}")
    return index

pindex = indexed(projects, "projects")
tindex = indexed(topics, "topics")
for pid, p in pindex.items():
    if p.get("verification") not in {"author-documented", "source-inspected", "reproduced", "unknown"}:
        errors.append(f"projects/{pid}: invalid verification")
    for tid in p.get("topics", []):
        if tid not in tindex:
            errors.append(f"projects/{pid}: unknown topic {tid}")
        elif pid not in tindex[tid].get("projects", []):
            errors.append(f"projects/{pid}: topic {tid} missing reciprocal link")
for tid, t in tindex.items():
    for pid in t.get("projects", []):
        if pid not in pindex:
            errors.append(f"topics/{tid}: unknown project {pid}")
        elif tid not in pindex[pid].get("topics", []):
            errors.append(f"topics/{tid}: project {pid} missing reciprocal link")
for r in rels:
    if r.get("from") not in pindex or r.get("to") not in pindex:
        errors.append(f"relationships: invalid endpoints {r}")
    if not isinstance(r.get("evidence"), str) or not r["evidence"].startswith("https://"):
        errors.append(f"relationships: missing evidence URL {r}")

for error in errors:
    print("ERROR:", error)
print(f"Checked {len(pindex)} projects, {len(tindex)} topics, {len(rels)} relationships.")
sys.exit(1 if errors else 0)
