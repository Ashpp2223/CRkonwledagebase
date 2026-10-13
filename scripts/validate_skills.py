#!/usr/bin/env python3
"""Validate repository-local Agent Skills metadata and required workflow coverage."""
from __future__ import annotations

from pathlib import Path
import re
import sys

import yaml

ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / ".agents" / "skills"
EXPECTED = {"curate-cr-knowledge", "review-cr-evidence", "review-cr-pr"}
NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
issues: list[str] = []

if not SKILLS_ROOT.is_dir():
    issues.append(f"Skill directory missing: {SKILLS_ROOT}")
    folders = []
else:
    folders = sorted(p for p in SKILLS_ROOT.iterdir() if p.is_dir())

seen = set()
for folder in folders:
    file = folder / "SKILL.md"
    if not file.is_file():
        issues.append(f"{folder.name}: missing SKILL.md")
        continue
    content = file.read_text(encoding="utf-8")
    if not content.startswith("---\n"):
        issues.append(f"{folder.name}: expected YAML front matter at document start")
        continue
    parts = content.split("---\n", 2)
    if len(parts) != 3:
        issues.append(f"{folder.name}: incomplete YAML front matter")
        continue
    try:
        meta = yaml.safe_load(parts[1])
    except yaml.YAMLError as exc:
        issues.append(f"{folder.name}: invalid YAML: {exc}")
        continue
    if not isinstance(meta, dict):
        issues.append(f"{folder.name}: metadata must be a mapping")
        continue
    name = meta.get("name")
    description = meta.get("description")
    if not isinstance(name, str) or not NAME.fullmatch(name) or len(name) > 64:
        issues.append(f"{folder.name}: invalid name")
    if name != folder.name:
        issues.append(f"{folder.name}: name does not match skill folder")
    if name in seen:
        issues.append(f"{folder.name}: duplicate skill name")
    seen.add(name)
    if not isinstance(description, str) or not description.strip() or len(description) > 1024:
        issues.append(f"{folder.name}: missing or overly long description")
    if len(parts[2].strip()) < 100:
        issues.append(f"{folder.name}: workflow body is missing or too short")
    for field, limit in (("compatibility", 500),):
        val = meta.get(field)
        if val is not None and (not isinstance(val, str) or len(val) > limit):
            issues.append(f"{folder.name}: invalid {field}")
    if "allowed-tools" in meta and not isinstance(meta["allowed-tools"], str):
        issues.append(f"{folder.name}: allowed-tools must be a string when specified")

missing = EXPECTED.difference(seen)
if missing:
    issues.append("missing baseline maintenance skills: " + ", ".join(sorted(missing)))

for issue in issues:
    print("ERROR:", issue)
print(f"Verified {len(seen)} repository skills, {len(issues)} issue(s).")
sys.exit(1 if issues else 0)
