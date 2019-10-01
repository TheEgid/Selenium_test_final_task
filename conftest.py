import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome',
                        help="Choise browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose language:")


@pytest.fixture(scope="function")
def browser(request):
    _language = request.config.getoption("language")
    _browser = request.config.getoption('browser')
    if _browser == 'chrome':
        options = Options()
        options.add_experimental_option(
            'prefs', {'intl.accept_languages': _language}
        )
        print(f"\nstart {_browser} for test..")
        browser = webdriver.Chrome(options=options)
    elif _browser == 'firefox':
        print(f"\nstart {_browser} for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", _language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError('--{_browser} should be chrome or firefox')
    yield browser

    print("\nquit browser..")
    browser.quit()
