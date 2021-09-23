import pytest

def pytest_addoption(parser):
    parser.addoption("--port", action="append", help="server port number")
    parser.addoption("--url", action="append", help="server url")

@pytest.fixture(scope="session")
def port(request):
    value = request.config.getoption("--port")
    if value is None:
        pytest.skip()
    return value

@pytest.fixture(scope="class")
def driver_class(request, port):
    class Driver:
        def __init__(self):
            self.port = port
    request.cls.setup = Driver()