#!/usr/bin/env python3
"""Validate every registry row against its JSON Schema (schema/*.schema.json)."""
import yaml, json, sys, os

try:
    import jsonschema
except ImportError:
    print(json.dumps({"check": "validate_schema", "status": "ERROR",
                       "reason": "jsonschema package not installed (pip install jsonschema)"}))
    sys.exit(2)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PAIRS = [
    ("macroareas.yaml", "macroarea.schema.json"),
    ("domains.yaml", "domain.schema.json"),
    ("portfolio.yaml", "portfolio.schema.json"),
    ("templates.yaml", "template.schema.json"),
    ("artifacts.yaml", "artifact.schema.json"),
    ("fields.yaml", "field.schema.json"),
    ("dependencies.yaml", "dependency.schema.json"),
    ("gates.yaml", "gate.schema.json"),
    ("evidence.yaml", "evidence.schema.json"),
    ("documents.yaml", "document.schema.json"),
    ("decisions.yaml", "decision.schema.json"),
    ("gaps.yaml", "gap.schema.json"),
    ("conflicts.yaml", "conflict.schema.json"),
    ("sources.yaml", "source.schema.json"),
]

errors = []
total_rows = 0
for registry_file, schema_file in PAIRS:
    rows = yaml.safe_load(open(os.path.join(ROOT, "registry", registry_file))) or []
    schema = json.load(open(os.path.join(ROOT, "schema", schema_file)))
    for i, row in enumerate(rows):
        total_rows += 1
        try:
            jsonschema.validate(row, schema)
        except jsonschema.ValidationError as e:
            errors.append(f"{registry_file}[{i}] ({row.get(list(row.keys())[0], '?')}): {e.message}")

result = {
    "check": "validate_schema",
    "total_rows_validated": total_rows,
    "schema_errors": errors[:50],
    "schema_error_count": len(errors),
    "status": "FAIL" if errors else "PASS",
}
print(json.dumps(result, indent=2, ensure_ascii=False))
sys.exit(1 if errors else 0)
