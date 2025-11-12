
URL="https://practicetestautomation.com/practice-test-login/ "

def test_page_title(setup):
 driver=setup
 driver.get(URL)
 assert "Test Login" in driver.title 

