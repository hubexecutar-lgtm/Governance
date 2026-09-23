def test_no_duplicate_canonical_ids(macroareas, domains, portfolio, artifacts, gates):
    ids = (
        [m["macroarea_id"] for m in macroareas]
        + [d["domain_id"] for d in domains]
        + [p["portfolio_id"] for p in portfolio]
        + [a["artifact_id"] for a in artifacts]
        + [g["gate_id"] for g in gates]
    )
    dupes = [x for x in set(ids) if ids.count(x) > 1]
    assert dupes == []


def test_no_orphan_field_instance_ids(fields, artifacts):
    artifact_ids = {a["artifact_id"] for a in artifacts}
    orphans = [f["field_instance_id"] for f in fields if f["artifact_id"] not in artifact_ids]
    assert orphans == []


def test_legacy_ids_mapped(artifacts, legacy_id_map):
    mapped = {r["legacy_id"] for r in legacy_id_map}
    unmapped = [lid for a in artifacts for lid in a.get("legacy_ids", []) if lid not in mapped]
    assert unmapped == []


def test_aliases_unambiguous(legacy_id_map):
    seen = {}
    conflicts = []
    for r in legacy_id_map:
        lid, cid = r["legacy_id"], r["canonical_id"]
        if lid in seen and seen[lid] != cid:
            conflicts.append(lid)
        seen[lid] = cid
    assert conflicts == []
