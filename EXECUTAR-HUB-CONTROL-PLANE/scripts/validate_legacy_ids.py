#!/usr/bin/env python3
"""Validate that every artifact's legacy_ids are represented in the legacy-id-map,
and that no legacy_id maps to more than one distinct canonical_id."""
import yaml, json, sys, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load(name):
    return yaml.safe_load(open(os.path.join(ROOT, "registry", name))) or []

artifacts = load("artifacts.yaml")
legacy_map = load("legacy-id-map.yaml")

map_by_legacy = {}
conflicting = []
for row in legacy_map:
    lid = row["legacy_id"]
    cid = row["canonical_id"]
    if lid in map_by_legacy and map_by_legacy[lid] != cid:
        conflicting.append({"legacy_id": lid, "mapped_to": [map_by_legacy[lid], cid]})
    map_by_legacy[lid] = cid

unmapped = []
for a in artifacts:
    for lid in a.get("legacy_ids", []):
        if lid not in map_by_legacy:
            unmapped.append({"artifact_id": a["artifact_id"], "unmapped_legacy_id": lid})

result = {
    "check": "validate_legacy_ids",
    "total_legacy_ids": len(legacy_map),
    "unmapped_legacy_ids": unmapped,
    "conflicting_mappings": conflicting,
    "status": "FAIL" if (unmapped or conflicting) else "PASS",
}
print(json.dumps(result, indent=2, ensure_ascii=False))
sys.exit(1 if (unmapped or conflicting) else 0)
