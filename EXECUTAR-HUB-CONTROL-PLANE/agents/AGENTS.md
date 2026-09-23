# Agents — EXECUTAR HUB Control Plane

Este diretório declara os agentes operacionais do control plane. Cada agente
é uma unidade de responsabilidade única (single-writer por escopo), nunca
inventa que uma etapa foi executada, e só reporta `VERIFIED` com evidência
real (saída de um dos `scripts/validate_*.py`).

| Agente | Papel |
|---|---|
| `orchestrator/` | Lê estado, resolve dependências, seleciona o próximo nó executável (WIP=1), executa, verifica, registra evidência. |
| `sheet-sync/` | Compara o snapshot `migrations/hub_model.snapshot.json` (derivado do Sheets congelado) com `registry/*.yaml`. |
| `schema-validator/` | Roda `scripts/validate_schema.py` contra todos os registries. |
| `dependency-resolver/` | Roda `scripts/validate_dependencies.py` e `scripts/validate_gates.py`. |
| `artifact-manager/` | Lê/atualiza `registry/artifacts.yaml` e `registry/fields.yaml` — único writer autorizado desses arquivos. |
| `document-builder/` | Gera `views/*.yaml` e prepara os documentos finais (`Axx-FINAL-001`, `Mxx-FINAL-001`, `EXECUTAR-FINAL-001`) a partir de `views/`. |
| `audit/` | Roda `scripts/generate_reports.py` e publica `reports/parity-report.md`. |

Todo agente declara `reads`, `writes`, `tools`, `permissions` no seu `config.yaml` —
um agente nunca escreve fora do escopo declarado.
