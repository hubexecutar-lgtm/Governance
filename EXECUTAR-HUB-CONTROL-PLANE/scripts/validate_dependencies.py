#!/usr/bin/env python3
"""Validate that every dependency edge points to an existing artifact_id,
and that there are no direct self-referencing cycles (A depends_on A)."""
import yaml, json, sys, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load(name):
    return yaml.safe_load(open(os.path.join(ROOT, "registry", name))) or []

artifacts = load("artifacts.yaml")
dependencies = load("dependencies.yaml")
artifact_ids = {a["artifact_id"] for a in artifacts}

orphans = []
self_cycles = []
for dep in dependencies:
    if dep["source_artifact_id"] not in artifact_ids:
        orphans.append({"dependency_id": dep["dependency_id"], "missing": dep["source_artifact_id"], "field": "source_artifact_id"})
    if dep["target_artifact_id"] not in artifact_ids:
        orphans.append({"dependency_id": dep["dependency_id"], "missing": dep["target_artifact_id"], "field": "target_artifact_id"})
    if dep["source_artifact_id"] == dep["target_artifact_id"]:
        self_cycles.append(dep["dependency_id"])

result = {
    "check": "validate_dependencies",
    "total_dependencies": len(dependencies),
    "broken_dependencies": orphans,
    "self_cycles": self_cycles,
    "status": "FAIL" if (orphans or self_cycles) else "PASS",
}
print(json.dumps(result, indent=2, ensure_ascii=False))
sys.exit(1 if (orphans or self_cycles) else 0)
