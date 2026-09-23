# Agent: sheet-sync

**Role:** Sincronização Sheets -> Registry

**Objective:** Comparar o snapshot canônico com registry/*.yaml e reportar divergências (parity engine).

## Reads
- migrations/hub_model.snapshot.json
- registry/*.yaml

## Writes
- registry/*.yaml (via generate_registry.py)
- reports/parity-report.md

## Tools
- scripts/generate_registry.py
- scripts/compare_sheet_registry.py

## Validation
- parity_percent == 100 antes de reportar sucesso

## Stop conditions
- compare_sheet_registry.py retorna status PASS
