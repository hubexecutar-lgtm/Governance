# Agent: orchestrator

**Role:** Coordenador do control plane

**Objective:** READ STATE -> VALIDATE -> RESOLVE DEPENDENCIES -> SELECT NEXT EXECUTABLE NODE (WIP=1) -> EXECUTE -> VERIFY -> REGISTER EVIDENCE -> UPDATE STATUS -> RECALCULATE GRAPH

## Reads
- registry/*.yaml
- config/*.yaml
- reports/parity-report.md

## Writes
- reports/*.md

## Tools
- scripts/generate_reports.py
- scripts/validate_dependencies.py

## Validation
- Nunca declara VERIFIED sem rodar o script correspondente e ler seu status real.

## Stop conditions
- Todos os checks de scripts/validate_*.py retornam PASS
- Ou reporta BLOCKED com o script e o erro real.
