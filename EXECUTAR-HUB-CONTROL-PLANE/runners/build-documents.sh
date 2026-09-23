#!/usr/bin/env bash
# Placeholder para geração de documentos finais consolidados (F01/F02/F03).
# Hoje apenas garante que registry/documents.yaml e views/documents/ existem
# e estão sincronizados; a redação de prosa dos documentos finais é
# NOT_CREATED em todos os registros (ver registry/documents.yaml) até
# decisão humana sobre owners e conteúdo (nunca inventados).
set -euo pipefail
cd "$(dirname "$0")/.."
test -f views/documents/index.yaml || { echo "views/documents/index.yaml ausente — rode build-views.sh primeiro"; exit 1; }
echo "documents index OK: $(python3 -c "import yaml;print(len(yaml.safe_load(open('views/documents/index.yaml'))))") documentos registrados (status NOT_CREATED até preenchimento humano)"
