import subprocess, json, os, sys, pytest

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def test_compare_sheet_registry_runs_without_sheet():
    """Without a --sheet snapshot the script must report BLOCKED, never a
    fabricated PASS — this test guards against silently faking parity."""
    p = subprocess.run(
        [sys.executable, os.path.join(ROOT, "scripts", "compare_sheet_registry.py")],
        capture_output=True, text=True,
    )
    assert p.returncode == 2  # BLOCKED_NO_SHEET_SNAPSHOT


@pytest.mark.skipif(
    not os.environ.get("SHEET_SNAPSHOT_PATH"),
    reason="set SHEET_SNAPSHOT_PATH to the frozen .xlsx to run real parity check",
)
def test_full_parity_against_sheet_snapshot():
    p = subprocess.run(
        [sys.executable, os.path.join(ROOT, "scripts", "compare_sheet_registry.py"),
         "--sheet", os.environ["SHEET_SNAPSHOT_PATH"]],
        capture_output=True, text=True,
    )
    result = json.loads(p.stdout)
    assert result["status"] == "PASS"
    assert result["parity_percent"] == 100.0
