#!/usr/bin/env bash
# Mesmo status de build-documents.sh: dossiês finais dependem de conteúdo
# humano (owners, riscos, métricas) que este runner não inventa.
set -euo pipefail
cd "$(dirname "$0")/.."
echo "BLOCKED: dossiês finais (Axx-FINAL-001, Mxx-FINAL-001, EXECUTAR-FINAL-001) exigem preenchimento humano via Google Sheets antes de consolidação. Ver registry/documents.yaml (status=NOT_CREATED)."
exit 2
