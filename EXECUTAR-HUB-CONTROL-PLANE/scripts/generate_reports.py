#!/usr/bin/env python3
"""Run every validate_*.py + compare_sheet_registry.py and write
reports/parity-report.md with the REAL results (never simulated)."""
import subprocess, json, sys, os, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHECKS = [
    "validate_ids.py", "validate_dependencies.py", "validate_orphans.py",
    "validate_gates.py", "validate_links.py", "validate_legacy_ids.py",
    "validate_schema.py",
]

def run(script, extra_args=None):
    cmd = [sys.executable, os.path.join(ROOT, "scripts", script)] + (extra_args or [])
    p = subprocess.run(cmd, capture_output=True, text=True)
    try:
        out = json.loads(p.stdout)
    except json.JSONDecodeError:
        out = {"raw_stdout": p.stdout, "raw_stderr": p.stderr}
    out["returncode"] = p.returncode
    return out

def main():
    sheet_path = sys.argv[1] if len(sys.argv) > 1 else None
    results = {c: run(c) for c in CHECKS}
    results["compare_sheet_registry.py"] = run("compare_sheet_registry.py", ["--sheet", sheet_path] if sheet_path else [])

    lines = [
        "# Parity / Validation Report — EXECUTAR HUB Control Plane",
        "",
        f"Gerado em: {datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')}",
        "",
        "| Check | Status | Detalhe |",
        "|---|---|---|",
    ]
    all_pass = True
    for name, r in results.items():
        status = r.get("status", "ERROR")
        if status not in ("PASS",):
            all_pass = False
        detail = ""
        if status == "FAIL":
            for k in ("duplicate_canonical_ids", "broken_dependencies", "orphan_records",
                      "missing_gate_references", "broken_links", "unmapped_legacy_ids", "canonical_id_mismatch"):
                if r.get(k):
                    detail = f"{k}: {r[k]}"
                    break
        elif status.startswith("BLOCKED"):
            detail = "Sem snapshot .xlsx fornecido — rode com `python3 scripts/generate_reports.py /path/to/sheet.xlsx`"
        lines.append(f"| {name} | {status} | {detail} |")

    lines += [
        "",
        "## Resultado bruto (JSON, para CI/agentes)",
        "```json",
        json.dumps(results, indent=2, ensure_ascii=False),
        "```",
    ]
    report = "\n".join(lines)
    with open(os.path.join(ROOT, "reports", "parity-report.md"), "w") as f:
        f.write(report)
    print(report)
    sys.exit(0 if all_pass else 1)

if __name__ == "__main__":
    main()
