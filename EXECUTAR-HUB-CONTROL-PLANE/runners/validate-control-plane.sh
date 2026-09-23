#!/usr/bin/env bash
# Roda todas as validações estruturais (não a paridade com Sheets).
set -euo pipefail
cd "$(dirname "$0")/.."
fail=0
for s in validate_ids validate_dependencies validate_orphans validate_gates validate_links validate_legacy_ids validate_schema; do
  echo "== $s =="
  python3 "scripts/${s}.py" || fail=1
done
exit $fail
