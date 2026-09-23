# Parity / Validation Report — EXECUTAR HUB Control Plane

Gerado em: 2026-09-23T13:13:55Z

| Check | Status | Detalhe |
|---|---|---|
| validate_ids.py | PASS |  |
| validate_dependencies.py | PASS |  |
| validate_orphans.py | PASS |  |
| validate_gates.py | PASS |  |
| validate_links.py | PASS |  |
| validate_legacy_ids.py | PASS |  |
| validate_schema.py | PASS |  |
| compare_sheet_registry.py | PASS |  |

## Resultado bruto (JSON, para CI/agentes)
```json
{
  "validate_ids.py": {
    "check": "validate_ids",
    "total_ids": 106,
    "duplicate_canonical_ids": [],
    "status": "PASS",
    "returncode": 0
  },
  "validate_dependencies.py": {
    "check": "validate_dependencies",
    "total_dependencies": 0,
    "broken_dependencies": [],
    "self_cycles": [],
    "status": "PASS",
    "returncode": 0
  },
  "validate_orphans.py": {
    "check": "validate_orphans",
    "total_artifacts": 37,
    "total_fields": 1125,
    "orphan_records": [],
    "status": "PASS",
    "returncode": 0
  },
  "validate_gates.py": {
    "check": "validate_gates",
    "total_gates": 12,
    "missing_gate_references": [],
    "status": "PASS",
    "returncode": 0
  },
  "validate_links.py": {
    "check": "validate_links",
    "broken_links": [],
    "status": "PASS",
    "returncode": 0
  },
  "validate_legacy_ids.py": {
    "check": "validate_legacy_ids",
    "total_legacy_ids": 37,
    "unmapped_legacy_ids": [],
    "conflicting_mappings": [],
    "status": "PASS",
    "returncode": 0
  },
  "validate_schema.py": {
    "check": "validate_schema",
    "total_rows_validated": 1370,
    "schema_errors": [],
    "schema_error_count": 0,
    "status": "PASS",
    "returncode": 0
  },
  "compare_sheet_registry.py": {
    "check": "compare_sheet_registry",
    "parity": {
      "macroareas": {
        "github_count": 13,
        "sheets_count": 13,
        "missing_in_github": [],
        "extra_in_github": []
      },
      "domains": {
        "github_count": 24,
        "sheets_count": 24,
        "missing_in_github": [],
        "extra_in_github": []
      },
      "portfolio": {
        "github_count": 20,
        "sheets_count": 20,
        "missing_in_github": [],
        "extra_in_github": []
      },
      "templates": {
        "github_count": 20,
        "sheets_count": 20,
        "missing_in_github": [],
        "extra_in_github": []
      },
      "artifacts": {
        "github_count": 37,
        "sheets_count": 37,
        "missing_in_github": [],
        "extra_in_github": []
      },
      "fields": {
        "github_count": 1125,
        "sheets_count": 1125,
        "missing_in_github": [],
        "extra_in_github": []
      },
      "dependencies": {
        "github_count": 0,
        "sheets_count": 0,
        "missing_in_github": [],
        "extra_in_github": []
      },
      "gates": {
        "github_count": 12,
        "sheets_count": 12,
        "missing_in_github": [],
        "extra_in_github": []
      }
    },
    "canonical_id_mismatch": [],
    "parity_percent": 100.0,
    "status": "PASS",
    "returncode": 0
  }
}
```