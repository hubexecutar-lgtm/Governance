import json, os
import pytest

jsonschema = pytest.importorskip("jsonschema")

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PAIRS = [
    ("macroareas.yaml", "macroarea.schema.json"),
    ("domains.yaml", "domain.schema.json"),
    ("portfolio.yaml", "portfolio.schema.json"),
    ("templates.yaml", "template.schema.json"),
    ("artifacts.yaml", "artifact.schema.json"),
    ("fields.yaml", "field.schema.json"),
    ("dependencies.yaml", "dependency.schema.json"),
    ("gates.yaml", "gate.schema.json"),
]


@pytest.mark.parametrize("registry_file,schema_file", PAIRS)
def test_registry_matches_schema(registry_file, schema_file):
    import yaml
    rows = yaml.safe_load(open(os.path.join(ROOT, "registry", registry_file))) or []
    schema = json.load(open(os.path.join(ROOT, "schema", schema_file)))
    for row in rows:
        jsonschema.validate(row, schema)


def test_no_invalid_schema_files():
    schema_dir = os.path.join(ROOT, "schema")
    for fn in os.listdir(schema_dir):
        if fn.endswith(".schema.json"):
            json.load(open(os.path.join(schema_dir, fn)))  # raises if malformed
