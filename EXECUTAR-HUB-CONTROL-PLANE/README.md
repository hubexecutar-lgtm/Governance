# EXECUTAR — HUB Control Plane

Espelho estrutural, versionado e executável do control plane matricial do
programa EXECUTAR. **A fonte primária de verdade é o Google Sheets** — este
repositório é `CODE_MIRROR_AND_VERSIONED_SCHEMA` (ver `config/sync.yaml`).

- **Google Sheets (fonte primária, congelado):** https://docs.google.com/spreadsheets/d/1AlEgMNGSBpgJBkgeqdFzlKWeez8ftSko/edit
- **schema_version:** 1.0.0 — congelado em `config/schema.yaml`
- **ADR:** ADR-EXECUTAR-HUB-001

## Arquitetura

```
PROGRAMA (EXECUTAR)
  └─ MACROÁREAS (Axx)         registry/macroareas.yaml   — 13 registros
       └─ DOMÍNIOS (Dxx)      registry/domains.yaml      — 24 registros
  PORTFÓLIO (Mxx)             registry/portfolio.yaml    — 20 registros  (eixo independente, cruza com artefatos)
       └─ ARTEFATOS           registry/artifacts.yaml    — 37 registros
            └─ CAMPOS         registry/fields.yaml       — 1125 registros
  DEPENDÊNCIAS (edges)        registry/dependencies.yaml — 0 (não reconciliadas na fonte, ver GAP-DEP-01)
  GATES                       registry/gates.yaml        — 12 registros (G00–G11)
  DOCUMENTOS FINAIS           registry/documents.yaml    — 34 registros (F01/F02/F03)
```

Macroárea e Domínio são capacidades permanentes; Portfólio é o eixo de
produtos/iniciativas; eles se cruzam através de Artefatos (C07). Template e
Instância são entidades diferentes (C06) — ver `templates/` vs.
`registry/artifacts.yaml#template_id`.

## IDs

Todo `canonical_id` deste repositório é **idêntico** ao `canonical_id` da
aba correspondente no Google Sheets (`GITHUB ID INVARIANT`). IDs legados
nunca são apagados, reciclados ou renumerados — ver
`registry/legacy-id-map.yaml` e `migrations/legacy-to-v1.yaml`.

## Relação Sheets ↔ GitHub

```
GOOGLE SHEETS (fonte operacional)
      │  export manual → migrations/hub_model.snapshot.json
      ▼
scripts/generate_registry.py  →  registry/*.yaml
scripts/generate_views.py     →  views/*.yaml (projeções somente-leitura)
scripts/compare_sheet_registry.py --sheet <snapshot.xlsx>  →  reports/parity-report.md
```

Não existe sincronização automática bidirecional nesta versão — o Sheets é
editado por humanos; o GitHub é regenerado a partir de um snapshot exportado
do Sheets. Ver `OPERATIONS.md` para o passo a passo.

## Instalação

```bash
pip install -r requirements.txt
```

## Execução

```bash
bash runners/validate-control-plane.sh      # todas as validações estruturais
bash runners/audit-parity.sh /path/to/sheet.xlsx   # paridade real vs. um snapshot do Sheets
python3 -m pytest tests/ -q                 # suíte de testes
```

## Manutenção

Sempre que o Sheets mudar: exporte um novo `hub_model.snapshot.json` (ou um
`.xlsx`), rode `scripts/generate_registry.py` e `scripts/generate_reports.py`,
e commite o diff — nunca edite `registry/*.yaml` manualmente fora desse fluxo
(regra DATA_01: um fato é armazenado uma única vez).

Ver também: `ARCHITECTURE.md`, `GOVERNANCE.md`, `OPERATIONS.md`,
`SECURITY.md`, `CONTRIBUTING.md`, `MIGRATION.md`, `agents/AGENTS.md`.
