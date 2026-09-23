# Agent: dependency-resolver

**Role:** Integridade de dependências e gates

**Objective:** Garantir que toda dependência aponta para um artefato existente e todo gate_id referenciado existe.

## Reads
- registry/dependencies.yaml
- registry/artifacts.yaml
- registry/gates.yaml

## Writes


## Tools
- scripts/validate_dependencies.py
- scripts/validate_gates.py

## Validation
- broken_dependencies == [] e missing_gate_references == []

## Stop conditions
- ambos os scripts retornam PASS
