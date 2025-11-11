from selenium.webdriver.common.by import By

URL = "https://practicetestautomation.com/practice-test-login/"

def test_valid_login(setup):
    """✅ Test valid login functionality."""
    driver = setup
    driver.get(URL)

    # Enter valid credentials
    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("Password123")

    # Click submit button
    driver.find_element(By.ID, "submit").click()

    # Verify success message
    message = driver.find_element(By.TAG_NAME, "h1").text
    assert "Logged In Successfully" in message, "Login should be successful"
