from selenium.webdriver.common.by import By

URL="https://practicetestautomation.com/practice-test-login/"

def test_submit_visible(setup):
 
  driver=setup
  driver.get(URL)
  submit_button = driver. find_element(By.ID,"submit")
  assert  submit_button.is_displayed(), "Submit button is visible"
