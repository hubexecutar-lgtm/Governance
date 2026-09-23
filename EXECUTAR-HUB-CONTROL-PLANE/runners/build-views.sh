#!/usr/bin/env bash
# Gera views/*.yaml a partir de registry/*.yaml.
set -euo pipefail
cd "$(dirname "$0")/.."
python3 scripts/generate_views.py
