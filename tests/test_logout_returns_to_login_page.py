from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://practicetestautomation.com/practice-test-login/"

def test_logout_returns_to_login_page(setup):
    """↩️ Validate that logout redirects back to login page."""
    driver = setup
    driver.get(URL)
    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()

    logout_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='Log out']"))
    )
    logout_button.click()

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "submit")))
    assert "Test Login" in driver.title, "After logout, user should return to login page"
