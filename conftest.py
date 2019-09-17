import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='es',
                     help="Choose language: es is default")


@pytest.fixture(scope="function")
def browser(request):
    browser = None
    browser_name = request.config.getoption("browser_name")
    _language = request.config.getoption("language")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': _language})
        options.add_experimental_option('w3c', False)
        browser = webdriver.Chrome(options=options) #,
                                   #executable_path=r'C:\\chromedriver\chromedriver.exe')
        browser.implicitly_wait(5)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", _language)
        browser = webdriver.Firefox(firefox_profile=fp)
        browser.implicitly_wait(5)
    else:
        print("Browser {} still is not implemented".format(browser_name))
    yield browser
    print("\nquit browser..")
    browser.quit()
