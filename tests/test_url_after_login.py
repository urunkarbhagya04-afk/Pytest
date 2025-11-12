from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
URL="https://practicetestautomation.com/practice-test-login/"


def  test_url_after_login(setup):
 driver=setup
 driver.get(URL)
 driver.find_element(By.ID,"username").send_keys("student")
 driver.find_element(By.ID,"password").send_keys("Password123")
 driver.find_element(By.ID,"submit").click()
 
 WebDriverWait(driver, 5).until(EC.url_contains("logged-in-successfully"))
 assert "logged-in-successfully" in driver.current_url, "Should redirect to success URL"



 
