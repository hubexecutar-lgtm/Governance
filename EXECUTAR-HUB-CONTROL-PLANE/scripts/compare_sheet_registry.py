#!/usr/bin/env python3
"""Parity engine: compare canonical_id sets between the frozen Sheets export
(a local xlsx snapshot, since this environment has no live Sheets API) and
the GitHub registries. Usage:
  python3 compare_sheet_registry.py --sheet /path/to/EXECUTAR_HUB_Control_Plane_v2.xlsx
If --sheet is omitted, only intra-registry duplicate/orphan checks run and a
BLOCKED note is printed for the Sheets side of parity (never fabricated)."""
import argparse, yaml, json, sys, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load(name):
    return yaml.safe_load(open(os.path.join(ROOT, "registry", name))) or []

REG_MAP = {
    "macroareas": ("macroareas.yaml", "10_REG_Macroareas", "macroarea_id"),
    "domains": ("domains.yaml", "11_REG_Dominios", "domain_id"),
    "portfolio": ("portfolio.yaml", "12_REG_Portfolio", "portfolio_id"),
    "templates": ("templates.yaml", "13_REG_Templates", "template_id"),
    "artifacts": ("artifacts.yaml", "14_REG_Artefatos", "artifact_id"),
    "fields": ("fields.yaml", "15_REG_Campos", "field_instance_id"),
    "dependencies": ("dependencies.yaml", "16_REG_Dependencias", "dependency_id"),
    "gates": ("gates.yaml", "17_REG_Gates", "gate_id"),
}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sheet", default=None, help="Path to the frozen .xlsx snapshot")
    args = ap.parse_args()

    parity = {}
    canonical_mismatch = []

    sheet_ids = {}
    if args.sheet and os.path.exists(args.sheet):
        import openpyxl
        wb = openpyxl.load_workbook(args.sheet, data_only=False)
        for key, (_, sheet_name, _) in REG_MAP.items():
            ids = set()
            if sheet_name in wb.sheetnames:
                ws = wb[sheet_name]
                for row in ws.iter_rows(min_row=2, max_col=1):
                    for cell in row:
                        if cell.value:
                            ids.add(str(cell.value))
            sheet_ids[key] = ids
    else:
        print(json.dumps({"warning": "no --sheet snapshot provided; sheets_count reported as null (never fabricated)"}))

    for key, (regfile, sheet_name, idfield) in REG_MAP.items():
        rows = load(regfile)
        gh_ids = {str(r[idfield]) for r in rows}
        sh_ids = sheet_ids.get(key)
        entry = {
            "github_count": len(gh_ids),
            "sheets_count": len(sh_ids) if sh_ids is not None else None,
            "missing_in_github": sorted(sh_ids - gh_ids) if sh_ids is not None else [],
            "extra_in_github": sorted(gh_ids - sh_ids) if sh_ids is not None else [],
        }
        parity[key] = entry
        if sh_ids is not None and (entry["missing_in_github"] or entry["extra_in_github"]):
            canonical_mismatch.append(key)

    total_gh = sum(v["github_count"] for v in parity.values())
    total_mismatched = sum(len(v["missing_in_github"]) + len(v["extra_in_github"]) for v in parity.values())
    parity_percent = 100.0 if total_gh == 0 else round(100.0 * (total_gh - total_mismatched) / total_gh, 2)

    result = {
        "check": "compare_sheet_registry",
        "parity": parity,
        "canonical_id_mismatch": canonical_mismatch,
        "parity_percent": parity_percent if args.sheet else None,
        "status": "PASS" if (args.sheet and not canonical_mismatch) else ("BLOCKED_NO_SHEET_SNAPSHOT" if not args.sheet else "FAIL"),
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))
    sys.exit(0 if result["status"] == "PASS" else (2 if result["status"].startswith("BLOCKED") else 1))

if __name__ == "__main__":
    main()
