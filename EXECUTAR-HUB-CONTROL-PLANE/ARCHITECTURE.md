# Architecture

## Camadas

1. **Google Sheets** (`config/schema.yaml#source_sheet_id`) — superfície de
   preenchimento humano: 13 abas `01_Formulario_<Axx>` (uma por macroárea),
   fielmente ao padrão do workbook de referência original
   (`EXECUTAR_projetosaasentrypoint_EXPANDIDO.xlsx`): lista linear
   ID/Campo/Instrução/Resposta/Exemplo, única coluna editável (amarelo),
   sem dropdowns nem validação em cascata.
2. **`migrations/hub_model.snapshot.json`** — snapshot canônico do modelo,
   fonte única a partir da qual registries e views são gerados (garante
   paridade por construção).
3. **`registry/*.yaml`** — registro normalizado, 15 arquivos, um por
   entidade do modelo. Nunca editado manualmente — sempre via
   `scripts/generate_registry.py`.
4. **`views/*.yaml`** — projeções somente-leitura (por macroárea, por
   portfólio, documento) — nunca fonte de verdade (regra SOURCE_01).
5. **`schema/*.schema.json`** — contrato JSON Schema de cada entidade.
6. **`agents/`, `runners/`, `scripts/`** — automação executável.

## Entidades e relações

```
Macroárea 1───N Domínio
Portfólio (eixo independente)
Artefato  N───1 Macroárea, N───1 Domínio(opcional), N───1 Portfólio(opcional), N───1 Template(opcional)
Campo     N───1 Artefato
Dependência: edge explícito Artefato → Artefato (DEPENDS_ON | BLOCKS | PRODUCES | CONSUMES | DERIVES_FROM)
Gate: escopo PROGRAM | PORTFOLIO | ARTIFACT
Documento Final: nível MACROAREA | PORTFOLIO | PROGRAM, deriva de Artefatos
```

## Por que Template ≠ Instância (C06)

Um `template_id` (`registry/templates.yaml`) existe uma única vez. Cada
Artefato real (`registry/artifacts.yaml`) referencia um `template_id` via
`artifact.template_id`, mas tem seu próprio `artifact_id` — múltiplos
artefatos de produtos diferentes podem instanciar o mesmo template.

## Por que Portfólio não é filho de Macroárea (C07, PORTFOLIO_01/02)

`registry/portfolio.yaml` é um eixo independente de `registry/domains.yaml`.
Um item de portfólio consome capacidades de múltiplas macroáreas através dos
artefatos que ele possui (`artifact.portfolio_id` + `artifact.macroarea_id`
são campos independentes na mesma linha).

## Invariantes ativos (ver `INVARIANTS` no MASTER COMMAND original)

Todos os invariantes UX_*, ID_*, DATA_*, TEMPLATE_*, PORTFOLIO_*, DEP_*,
GATE_*, DOC_*, EVIDENCE_*, SOURCE_* são verificados, total ou parcialmente,
pelos scripts em `scripts/validate_*.py` e pelos testes em `tests/`. Nenhum
invariante é apenas documental sem verificação executável correspondente,
exceto onde marcado como dependente de preenchimento humano (ex.: DOC_01/02/03
— documentos finais ainda `NOT_CREATED`).
