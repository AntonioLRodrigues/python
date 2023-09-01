import pytest
from selenium import webdriver
driver: webdriver.Remote


@pytest.fixture
def setup_teardown():
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    yield
    driver.quit()
