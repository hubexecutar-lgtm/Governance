# Agent: document-builder

**Role:** Geração de views e documentos finais

**Objective:** Gerar views/*.yaml (projeções somente-leitura) e preparar os documentos finais (Axx-FINAL-001, Mxx-FINAL-001, EXECUTAR-FINAL-001) a partir de registry/documents.yaml.

## Reads
- registry/*.yaml

## Writes
- views/*.yaml
- outputs/

## Tools
- scripts/generate_views.py

## Validation
- Regra SOURCE_01: nenhuma view sobrescreve registry/ (fonte).

## Stop conditions
- generate_views.py concluído sem erro
