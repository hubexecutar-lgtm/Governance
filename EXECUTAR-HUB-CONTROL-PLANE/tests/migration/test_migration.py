import json, os


ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def test_snapshot_exists():
    assert os.path.exists(os.path.join(ROOT, "migrations", "hub_model.snapshot.json"))


def test_every_artifact_has_a_legacy_id(artifacts):
    missing = [a["artifact_id"] for a in artifacts if not a.get("legacy_ids")]
    assert missing == []


def test_no_lost_source_deliverables(artifacts):
    """The source YAML had 37 deliverables (metadata.summary.documents); this
    must never silently drop below that count."""
    assert len(artifacts) == 37
