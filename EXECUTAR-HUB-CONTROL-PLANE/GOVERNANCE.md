# Governance

## Autoridade

```yaml
authority:
  google_sheets: PRIMARY_OPERATIONAL_SOURCE
  github: VERSIONED_CODE_MIRROR
```

O GitHub nunca cria uma segunda fonte de verdade concorrente (C05). Qualquer
mudança estrutural começa no Sheets, é congelada (`config/schema.yaml`), e só
então espelhada aqui.

## Política de IDs

- `canonical_id` é imutável após o freeze (`config/id-policy.yaml`).
- `legacy_ids` são preservados indefinidamente — nunca apagados.
- Nenhum ID é reciclado, mesmo que o artefato original seja depreciado.

## Decisões

Toda decisão de governança (mapeamento de macroárea, desvios de UX, etc.)
é registrada em `registry/decisions.yaml` com `rationale` e
`requires_human_validation`. Decisões com `requires_human_validation: true`
não podem ser tratadas como aprovadas até revisão humana explícita.

## Conflitos e gaps

`registry/conflicts.yaml` (10 registros, herdados do corpus original) e
`registry/gaps.yaml` (10 registros) permanecem abertos até resolução humana
— nunca são silenciosamente fechados por este repositório.

## Owners

Todo campo `owner`/`approver` sem responsável real definido é `A_DEFINIR`
— nunca inventado.
