#!/usr/bin/env bash
# Regenera registry/*.yaml a partir de migrations/hub_model.snapshot.json.
set -euo pipefail
cd "$(dirname "$0")/.."
python3 scripts/generate_registry.py
