from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.mark.selenium
def test_google_title(driver):
    driver.get("https://www.google.com")
    print(f"Page title is: {driver.title}")
    assert driver.title == "Google"

def test_google_search(driver):
    driver.get("https://www.google.com")
    search_field = driver.find_element(By.NAME, "q") 
    search_field.send_keys("SOXL stock price")
    search_field.clear()  # Clear the search field before submitting
    print(f"Search field name: {search_field.get_attribute('name')}")
    print(f"Search field value: {search_field.get_attribute('aria-label')}")
    # search_field.submit()
    search_field.send_keys(Keys.ENTER)  # Press Enter to submit the search
