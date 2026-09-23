def test_dependency_targets_exist(dependencies, artifacts):
    artifact_ids = {a["artifact_id"] for a in artifacts}
    broken = [
        d["dependency_id"] for d in dependencies
        if d["source_artifact_id"] not in artifact_ids or d["target_artifact_id"] not in artifact_ids
    ]
    assert broken == []


def test_no_self_dependency(dependencies):
    cycles = [d["dependency_id"] for d in dependencies if d["source_artifact_id"] == d["target_artifact_id"]]
    assert cycles == []


def test_no_circular_dependency_pairs(dependencies):
    """A DEPENDS_ON B and B DEPENDS_ON A simultaneously is a forbidden 2-cycle."""
    edges = {(d["source_artifact_id"], d["target_artifact_id"]) for d in dependencies if d["relation"] == "DEPENDS_ON"}
    circular = [(a, b) for (a, b) in edges if (b, a) in edges]
    assert circular == []
