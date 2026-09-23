import os, sys, yaml, pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))


def load_registry(name):
    with open(os.path.join(ROOT, "registry", name)) as f:
        return yaml.safe_load(f) or []


@pytest.fixture(scope="session")
def macroareas():
    return load_registry("macroareas.yaml")


@pytest.fixture(scope="session")
def domains():
    return load_registry("domains.yaml")


@pytest.fixture(scope="session")
def portfolio():
    return load_registry("portfolio.yaml")


@pytest.fixture(scope="session")
def artifacts():
    return load_registry("artifacts.yaml")


@pytest.fixture(scope="session")
def fields():
    return load_registry("fields.yaml")


@pytest.fixture(scope="session")
def dependencies():
    return load_registry("dependencies.yaml")


@pytest.fixture(scope="session")
def gates():
    return load_registry("gates.yaml")


@pytest.fixture(scope="session")
def legacy_id_map():
    return load_registry("legacy-id-map.yaml")
