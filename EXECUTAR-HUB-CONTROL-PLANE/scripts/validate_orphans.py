#!/usr/bin/env python3
"""Validate referential integrity: every artifact.macroarea_id/domain_id/portfolio_id
and every field.artifact_id must point to an existing record."""
import yaml, json, sys, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load(name):
    return yaml.safe_load(open(os.path.join(ROOT, "registry", name))) or []

macroareas = {m["macroarea_id"] for m in load("macroareas.yaml")}
domains = {d["domain_id"] for d in load("domains.yaml")}
portfolio = {p["portfolio_id"] for p in load("portfolio.yaml")}
artifacts = load("artifacts.yaml")
artifact_ids = {a["artifact_id"] for a in artifacts}
fields = load("fields.yaml")

orphans = []
for a in artifacts:
    if a["macroarea_id"] not in macroareas and a["macroarea_id"] != "A_DEFINIR":
        orphans.append({"artifact_id": a["artifact_id"], "missing_macroarea_id": a["macroarea_id"]})
    if a.get("domain_id") and a["domain_id"] not in domains:
        orphans.append({"artifact_id": a["artifact_id"], "missing_domain_id": a["domain_id"]})
    if a.get("portfolio_id") and a["portfolio_id"] not in portfolio:
        orphans.append({"artifact_id": a["artifact_id"], "missing_portfolio_id": a["portfolio_id"]})

for f in fields:
    if f["artifact_id"] not in artifact_ids:
        orphans.append({"field_instance_id": f["field_instance_id"], "missing_artifact_id": f["artifact_id"]})

result = {
    "check": "validate_orphans",
    "total_artifacts": len(artifacts),
    "total_fields": len(fields),
    "orphan_records": orphans,
    "status": "FAIL" if orphans else "PASS",
}
print(json.dumps(result, indent=2, ensure_ascii=False))
sys.exit(1 if orphans else 0)
