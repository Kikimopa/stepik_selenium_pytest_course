import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None, help='Choose browser: chrome or firefox')


@pytest.fixture(scope="function")
def driver(request):
    driver_name = request.config.getoption("browser_name")
    driver = None
    if driver_name == "chrome":
        print("\nstart chrome browser for test..")
        driver = webdriver.Chrome(executable_path=r"D:\stepik_selenium_course\chromeDriver\chromedriver.exe")
    elif driver_name == "firefox":
        print("\nstart firefox browser for test..")
        driver = webdriver.Firefox(executable_path=r"D:\stepik_selenium_course\geckodriver\geckodriver.exe")
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield driver
    print("\nquit browser..")
    driver.close()
