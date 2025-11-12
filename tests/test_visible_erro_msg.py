"""
Test Case: Verify the error message box color and text color after invalid login attempt.
Purpose:
    - To ensure that the UI shows a visible red error message box with white text.
"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://practicetestautomation.com/practice-test-login/"

def test_error_message_color(setup):
    """
    Steps:
    1. Open login page.
    2. Enter valid username and invalid password.
    3. Click Submit.
    4. Verify error message box visibility.
    5. Check that text is white and background is red.
    """

    driver = setup
    driver.get(URL)

    # Enter credentials
    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("wrongpass")
    driver.find_element(By.ID, "submit").click()

    # Wait for error box
    error_box = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "error"))
    )
    assert error_box.is_displayed(), "❌ Error box not visible!"

    # Check CSS colors
    text_color = error_box.value_of_css_property("color")
    background_color = error_box.value_of_css_property("background-color")

    print(f"🔍 Text color: {text_color}, Background color: {background_color}")

    # Assert white text
    assert "255" in text_color, f"❌ Expected white text, got {text_color}"

    # Assert red background (allow small variations)
    assert any(c in background_color for c in ["rgb(228, 67, 75)", "rgb(227, 72, 72)", "red"]), \
        f"❌ Expected red background, got {background_color}"

    print("✅ Error message colors verified successfully!")

