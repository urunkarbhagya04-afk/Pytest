import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def setup():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--headless")  # remove this if you want to see the browser
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.mark.parametrize("username,password,expected", [
    ("student", "Password123", "Logged In Successfully"),
    ("student", "wrongpass", "Your password is invalid!"),
    ("wronguser", "Password123", "Your username is invalid!")
])
def test_login_cases(setup, username, password, expected):
    driver = setup
    driver.get("https://practicetestautomation.com/practice-test-login/")

    driver.find_element("id", "username").send_keys(username)
    driver.find_element("id", "password").send_keys(password)
    driver.find_element("id", "submit").click()

    if expected == "Logged In Successfully":
        assert "Logged In Successfully" in driver.page_source
    else:
        error_message = driver.find_element("id", "error").text
        assert expected in error_message

