import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

@pytest.fixture
def setup():
    """Fixture for browser setup and teardown.
    - Initializes Firefox WebDriver using geckodriver.
    - Maximizes window.
    - Yields driver instance for test use.
    - Quits browser after test completion.
    """
    options = Options()
    service = Service("/snap/bin/geckodriver")  # path to geckodriver
    driver = webdriver.Firefox(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

