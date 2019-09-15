import pytest


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
                     help="Choose language")


@pytest.fixture(scope="function")
def language(request):
    _language = request.config.getoption("language")
    yield _language
