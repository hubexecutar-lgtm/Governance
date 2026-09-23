# Migration

Ver `migrations/README.md`, `migrations/legacy-to-v1.yaml`,
`migrations/id-map.csv` e `migrations/migration-report.md` (também
duplicado em `reports/migration-report.md`) para o relatório completo com
números reais desta migração v1.0.0.

Resumo: 37 artefatos e 1125 campos migrados de
`EXECUTAR_CHECKLIST_D01-D23_GRANULAR.yaml` (derivado de
`EXECUTAR_MASTER_PREFILL_D01-D23.yaml`) para o modelo matricial, com 100%
dos `legacy_ids` preservados e identidade (nenhum `canonical_id` novo
inventado — os IDs de origem já seguiam o formato canônico `Dxx-DOC-XXX-001`).
