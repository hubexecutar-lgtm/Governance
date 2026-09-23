# Agent: schema-validator

**Role:** Validação de schema JSON

**Objective:** Garantir que cada linha de cada registry respeita seu JSON Schema em schema/.

## Reads
- registry/*.yaml
- schema/*.schema.json

## Writes


## Tools
- scripts/validate_schema.py

## Validation
- schema_error_count == 0

## Stop conditions
- validate_schema.py retorna status PASS
