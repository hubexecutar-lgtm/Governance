#!/usr/bin/env bash
# Uso: audit-parity.sh [/caminho/para/EXECUTAR_HUB_Control_Plane.xlsx]
set -euo pipefail
cd "$(dirname "$0")/.."
python3 scripts/generate_reports.py "${1:-}"
