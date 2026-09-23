#!/usr/bin/env python3
"""Validate that every gate_id referenced by an artifact or dependency exists in registry/gates.yaml."""
import yaml, json, sys, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load(name):
    return yaml.safe_load(open(os.path.join(ROOT, "registry", name))) or []

gates = {g["gate_id"] for g in load("gates.yaml")}
artifacts = load("artifacts.yaml")
dependencies = load("dependencies.yaml")

missing = []
for a in artifacts:
    if a.get("gate_id") and a["gate_id"] not in gates:
        missing.append({"artifact_id": a["artifact_id"], "missing_gate_id": a["gate_id"]})
for d in dependencies:
    if d.get("gate_id") and d["gate_id"] not in gates:
        missing.append({"dependency_id": d["dependency_id"], "missing_gate_id": d["gate_id"]})

result = {
    "check": "validate_gates",
    "total_gates": len(gates),
    "missing_gate_references": missing,
    "status": "FAIL" if missing else "PASS",
}
print(json.dumps(result, indent=2, ensure_ascii=False))
sys.exit(1 if missing else 0)
