# Contributing

1. Nunca edite `registry/*.yaml` diretamente — edite o Google Sheets, exporte
   um snapshot, atualize `migrations/hub_model.snapshot.json` e rode
   `scripts/generate_registry.py`.
2. Todo `canonical_id` novo precisa existir primeiro no Sheets (C04 — Sheets
   primeiro).
3. Antes de abrir um PR: `bash runners/validate-control-plane.sh && python3 -m pytest tests/ -q`.
4. Mudanças em `schema/*.schema.json` exigem atualizar o registry
   correspondente e rodar `scripts/validate_schema.py`.
5. Decisões de arquitetura (mapeamentos, desvios de UX) vão em
   `registry/decisions.yaml`, nunca só em mensagem de commit.
