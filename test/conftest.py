import os, pytest


def pytest_addoption(parser):
    parser.addoption("--ws_uri", action="store", default=os.environ.get('BLOXROUTE_WS_URI'))
    parser.addoption("--auth_header", action="store", default=os.environ.get('BLOXROUTE_AUTH_HEADER'))
    parser.addoption("--conn_attempts", action="store", default="5")
    parser.addoption("--notification_count", action="store", default="5")
    parser.addoption("--channel", action="store", default="newTxs")


@pytest.fixture(scope="session")
def ws_uri(pytestconfig):
    return pytestconfig.getoption("ws_uri")


@pytest.fixture(scope="session")
def auth_header(pytestconfig):
    return pytestconfig.getoption("auth_header")


@pytest.fixture(scope="session")
def conn_attempts(pytestconfig):
    return int(pytestconfig.getoption("conn_attempts"))


@pytest.fixture(scope="session")
def notification_count(pytestconfig):
    return int(pytestconfig.getoption("notification_count"))


@pytest.fixture(scope="session")
def channel(pytestconfig):
    return pytestconfig.getoption("channel")
