# Security

- Este repositório não armazena segredos, tokens ou credenciais. O acesso ao
  Google Sheets é gerenciado fora deste repositório (permissões do Drive).
- `owner`/`approver` em `registry/artifacts.yaml` são identificadores de
  responsabilidade organizacional, não credenciais.
- CI (`.github/workflows/`) roda apenas checagens de leitura sobre
  `registry/` e `schema/` — nenhum workflow tem permissão de escrita no
  Google Sheets ou de push automático.
- Reporte qualquer dado sensível encontrado incorretamente commitado
  removendo-o em um novo commit e, se necessário, reescrevendo o histórico
  via processo próprio do time (fora do escopo automatizado deste repo).
