from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL="https://practicetestautomation.com/practice-test-login/"

def test_logout_button_visible(setup):
 driver=setup
 driver.get(URL)
 driver.find_element(By.ID,"username").send_keys("student")
 driver.find_element(By.ID,"password").send_keys("Password123")
 driver.find_element(By.ID,"submit").click()
 
 logout_button= WebDriverWait(driver,5).until(
        EC.presence_of_element_located((By.XPATH, "//a[text()='Log out']"))
    )
 assert logout_button.is_displayed(), "Logout button should be visible"

