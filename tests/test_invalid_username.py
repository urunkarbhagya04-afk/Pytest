                                             
from selenium .webdriver.common.by import By

URL="https://practicetestautomation.com/practice-test-login/"

def test_invalid_username(setup):
  driver=setup
  driver.get(URL)
  driver.find_element(By.ID,"username").send_keys("bhagyashree")
  driver.find_element(By.ID,"password").send_keys("Password123")
  driver.find_element(By.ID,"submit").click()
  
  error_msg=driver.find_element(By.ID,"error").text
  assert "username is invalid" in error_msg
