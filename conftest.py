import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='Chrome')


def change_browser(request):
    browser_name = request.config.getoption('--browser', default='Chrome')
    if browser_name == 'Firefox':
        browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser_name == 'Chrome':
        browser = webdriver.Chrome(ChromeDriverManager().install())
    return browser


@pytest.fixture(scope='session')
def browser(request):
    browser = change_browser(request)
    yield browser
    browser.quit()
