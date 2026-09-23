# Migration Report — EXECUTAR HUB Control Plane v1.0.0

Gerado em: 2026-09-23T13:08:43Z
Fonte congelada (Google Sheets): https://docs.google.com/spreadsheets/d/1AlEgMNGSBpgJBkgeqdFzlKWeez8ftSko/edit

## Quantidades

| Métrica | Valor |
|---|---|
| Registros de origem (deliverables no YAML granular) | 37 |
| Migrados (preserved) | 37 |
| Criados (novos canonical_id sem origem legada) | 0 |
| Aliased | 0 |
| Merged | 0 |
| Split | 0 |
| Deprecated | 0 |
| Moved | 0 |
| Conflitos em aberto | 10 |
| Gaps em aberto | 10 |
| IDs legados preservados | 37 |
| IDs canônicos totais (macroáreas+domínios+portfólio+artefatos) | 94 |
| Órfãos | 0 |

## Classificação de reconciliação

Todos os 37 artefatos migrados foram classificados como **KEEP** — os
`deliverable_id` do YAML granular (`EXECUTAR_CHECKLIST_D01-D23_GRANULAR.yaml`)
já seguiam um formato canônico (`Dxx-DOC-XXX-001`), então foram preservados
sem alteração como `canonical_id`, com `legacy_ids: [mesmo_id]` (identidade).
Nenhum objeto foi classificado como DEPRECATE nesta migração — ver
`registry/conflicts.yaml` e `registry/gaps.yaml` para itens que ainda exigem
decisão humana antes de qualquer reclassificação futura.

## Decisões registradas (ver registry/decisions.yaml)
23 decisões registradas, incluindo:
- Mapeamento Domínio (Dxx) → Macroárea (Axx): proposto por similaridade semântica de nome, não confirmado explicitamente nas fontes originais — `requires_human_validation: true` em cada uma.
- Split de `01_Formulario` em 13 abas por macroárea (DEC-UX-01) — aprovado pelo usuário.
- `09_Indice_IDs` formula-driven em vez de estático como o original (DEC-UX-02) — aprovado pelo usuário.

## Limitações herdadas da fonte (não resolvidas por esta migração)
- 1013 de 1125 campos são `PROPOSED` (interpretação, não fato verificado) — herdado do corpus original.
- Dependências entre artefatos não reconciliadas na fonte (ver GAP-DEP-01).
