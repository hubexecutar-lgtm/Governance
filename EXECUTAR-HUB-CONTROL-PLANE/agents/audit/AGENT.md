# Agent: audit

**Role:** Auditoria final e relatório de paridade

**Objective:** Rodar todos os validate_*.py + compare_sheet_registry.py e publicar reports/parity-report.md com dados reais.

## Reads
- registry/*.yaml
- schema/*.schema.json
- migrations/hub_model.snapshot.json

## Writes
- reports/parity-report.md
- reports/migration-report.md

## Tools
- scripts/generate_reports.py

## Validation
- Nunca declara parity_percent sem rodar compare_sheet_registry.py de fato.

## Stop conditions
- Todos os checks retornam PASS, ou BLOCKED é reportado nominalmente.
