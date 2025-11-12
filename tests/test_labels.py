from selenium.webdriver.common.by import By

URL=" https://practicetestautomation.com/practice-test-login/  "

def test_labels_visible(setup):
  driver=setup
  driver.get(URL)
  username_label= driver.find_element(By.XPATH,"//label[@for='username']")
  password_label= driver.find_element(By.XPATH,"//label[@for='password']")
  assert username_label.is_displayed() and password_label.is_displayed(), "Both labels should be visible"
