#!/usr/bin/env python3
"""Validate that every template_id referenced by an artifact exists in registry/templates.yaml,
and that every artifact.evidence_ids entry exists in registry/evidence.yaml."""
import yaml, json, sys, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load(name):
    return yaml.safe_load(open(os.path.join(ROOT, "registry", name))) or []

templates = {t["template_id"] for t in load("templates.yaml")}
evidence = {e["evidence_id"] for e in load("evidence.yaml")}
artifacts = load("artifacts.yaml")

broken = []
for a in artifacts:
    if a.get("template_id") and a["template_id"] not in templates:
        broken.append({"artifact_id": a["artifact_id"], "missing_template_id": a["template_id"]})
    for eid in a.get("evidence_ids", []):
        if eid not in evidence:
            broken.append({"artifact_id": a["artifact_id"], "missing_evidence_id": eid})

result = {
    "check": "validate_links",
    "broken_links": broken,
    "status": "FAIL" if broken else "PASS",
}
print(json.dumps(result, indent=2, ensure_ascii=False))
sys.exit(1 if broken else 0)
