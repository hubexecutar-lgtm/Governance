#!/usr/bin/env python3
"""Regenerate registry/*.yaml from migrations/hub_model.snapshot.json.
This is the single source both registries and (originally) the Sheets
workbook were generated from — re-running this after editing the snapshot
keeps registries in sync without hand-editing YAML."""
import json, yaml, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model = json.load(open(os.path.join(ROOT, "migrations", "hub_model.snapshot.json")))

FILES = {
    "macroareas.yaml": "macroareas",
    "domains.yaml": "domains",
    "portfolio.yaml": "portfolio",
    "templates.yaml": "templates",
    "artifacts.yaml": "artifacts",
    "fields.yaml": "fields",
    "dependencies.yaml": "dependencies",
    "gates.yaml": "gates",
    "evidence.yaml": "evidence",
    "documents.yaml": "documents",
    "decisions.yaml": "decisions",
    "gaps.yaml": "gaps",
    "conflicts.yaml": "conflicts",
    "sources.yaml": "sources",
    "legacy-id-map.yaml": "legacy_id_map",
}

for filename, key in FILES.items():
    path = os.path.join(ROOT, "registry", filename)
    with open(path, "w") as f:
        yaml.safe_dump(model[key], f, allow_unicode=True, sort_keys=False, default_flow_style=False)
    print(f"wrote {filename} ({len(model[key])} rows)")
