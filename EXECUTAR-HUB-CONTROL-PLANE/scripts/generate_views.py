#!/usr/bin/env python3
"""Generate views/*.yaml — read-only per-scope projections of the registries
(program, per-macroarea, per-portfolio, documents), analogous to the
narrative-mirror sheets (03/04/05/08) in the Google Sheets workbook.
Never a second source of truth (SOURCE_01) — always derived here."""
import json, yaml, os
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model = json.load(open(os.path.join(ROOT, "migrations", "hub_model.snapshot.json")))

os.makedirs(os.path.join(ROOT, "views", "macroareas"), exist_ok=True)
os.makedirs(os.path.join(ROOT, "views", "portfolio"), exist_ok=True)
os.makedirs(os.path.join(ROOT, "views", "documents"), exist_ok=True)

artifacts_by_macro = defaultdict(list)
for a in model["artifacts"]:
    artifacts_by_macro[a["macroarea_id"]].append(a["artifact_id"])

with open(os.path.join(ROOT, "views", "program.yaml"), "w") as f:
    yaml.safe_dump({
        "program_id": "EXECUTAR",
        "macroareas": len(model["macroareas"]),
        "domains": len(model["domains"]),
        "portfolio_items": len(model["portfolio"]),
        "templates": len(model["templates"]),
        "artifacts": len(model["artifacts"]),
        "fields": len(model["fields"]),
        "dependencies": len(model["dependencies"]),
        "gates": len(model["gates"]),
        "gaps_open": sum(1 for g in model["gaps"] if g["status"] == "OPEN"),
        "conflicts_open": sum(1 for c in model["conflicts"] if c["status"] == "ABERTO"),
    }, f, allow_unicode=True, sort_keys=False)

for m in model["macroareas"]:
    mid = m["macroarea_id"]
    with open(os.path.join(ROOT, "views", "macroareas", f"{mid}.yaml"), "w") as f:
        yaml.safe_dump({
            "macroarea_id": mid, "name": m["name"],
            "artifact_ids": artifacts_by_macro.get(mid, []),
        }, f, allow_unicode=True, sort_keys=False)

for p in model["portfolio"]:
    pid = p["portfolio_id"]
    with open(os.path.join(ROOT, "views", "portfolio", f"{pid}.yaml"), "w") as f:
        yaml.safe_dump({"portfolio_id": pid, "name": p["name"], "type": p["type"]},
                        f, allow_unicode=True, sort_keys=False)

with open(os.path.join(ROOT, "views", "documents", "index.yaml"), "w") as f:
    yaml.safe_dump(model["documents"], f, allow_unicode=True, sort_keys=False)

print("views generated:", 1 + len(model["macroareas"]) + len(model["portfolio"]) + 1)
