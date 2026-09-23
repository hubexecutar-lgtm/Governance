#!/usr/bin/env python3
"""Validate canonical_id uniqueness across all registries.
Exit 0 on PASS, 1 on FAIL. Prints a JSON result for CI consumption."""
import yaml, json, sys, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load(name):
    return yaml.safe_load(open(os.path.join(ROOT, "registry", name))) or []

macroareas = load("macroareas.yaml")
domains = load("domains.yaml")
portfolio = load("portfolio.yaml")
artifacts = load("artifacts.yaml")
gates = load("gates.yaml")

ids = (
    [m["macroarea_id"] for m in macroareas]
    + [d["domain_id"] for d in domains]
    + [p["portfolio_id"] for p in portfolio]
    + [a["artifact_id"] for a in artifacts]
    + [g["gate_id"] for g in gates]
)
dupes = sorted({x for x in ids if ids.count(x) > 1})

result = {
    "check": "validate_ids",
    "total_ids": len(ids),
    "duplicate_canonical_ids": dupes,
    "status": "FAIL" if dupes else "PASS",
}
print(json.dumps(result, indent=2, ensure_ascii=False))
sys.exit(1 if dupes else 0)
