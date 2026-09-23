# Operations

## Ciclo de sincronização Sheets → GitHub

1. Alguém preenche as abas `01_Formulario_<Axx>` no Google Sheets.
2. Exporte o Sheets (Arquivo → Download → Microsoft Excel `.xlsx`) para
   obter um snapshot atual.
3. Rode a paridade real: `bash runners/audit-parity.sh /caminho/snapshot.xlsx`
   — isso escreve `reports/parity-report.md` com dados reais.
4. Se `parity_percent < 100`: reconcilie manualmente (o Sheets é a fonte —
   nunca sobrescreva um valor do Sheets com um valor do GitHub).
5. Se paridade OK e você atualizou `migrations/hub_model.snapshot.json` com
   os novos dados: `python3 scripts/generate_registry.py && python3 scripts/generate_views.py`.
6. Commit do diff em `registry/` e `views/`.

## Checagens de rotina

```bash
bash runners/validate-control-plane.sh   # todas as validações estruturais
python3 -m pytest tests/ -q               # suíte de testes
```

## Quando algo falha

Todo script de validação imprime JSON com `status: PASS|FAIL` e o motivo
específico (IDs duplicados, dependência quebrada, etc.) — nunca "silenciar"
uma falha. Um runner que não pode completar (ex.: `build-final-dossiers.sh`
sem conteúdo humano) retorna `BLOCKED` explicitamente com exit code 2, nunca
finge sucesso.
