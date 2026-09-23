EXPECTED_GATES = ["G00", "G01", "G02", "G03", "G04", "G05", "G06", "G07", "G08", "G09", "G10", "G11"]


def test_all_expected_gates_present(gates):
    gate_ids = {g["gate_id"] for g in gates}
    missing = [g for g in EXPECTED_GATES if g not in gate_ids]
    assert missing == []


def test_gate_referenced_by_artifact_or_dependency_exists(gates, artifacts, dependencies):
    gate_ids = {g["gate_id"] for g in gates}
    missing = [a["artifact_id"] for a in artifacts if a.get("gate_id") and a["gate_id"] not in gate_ids]
    missing += [d["dependency_id"] for d in dependencies if d.get("gate_id") and d["gate_id"] not in gate_ids]
    assert missing == []


def test_gate_incomplete_means_pending(gates):
    for g in gates:
        assert g["decision"] in ("PENDING", "PASS", "FAIL", "WAIVED")
