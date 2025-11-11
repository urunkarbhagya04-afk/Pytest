from selenium.webdriver.common.by import By
def test_invalid_password(setup):
    driver = setup
    driver.get("https://practicetestautomation.com/practice-test-login/")
    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("pass@123")  # ✅ fixed spelling
    driver.find_element(By.ID, "submit").click()
    error = driver.find_element(By.ID, "error").text
    assert "Your password is invalid!" in error

