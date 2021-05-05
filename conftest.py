import os
import sys
import pytest


myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')


def pytest_addoption(parser):
    parser.addoption('--url', action='store', default="https://ya.ru")
    parser.addoption('--status_code', action='store', default=200)


@pytest.fixture(scope="function")
def url(request):
    url = request.config.getoption("url")
    return url


@pytest.fixture(scope="function")
def status_code(request):
    status_code = request.config.getoption("status_code")
    return status_code
