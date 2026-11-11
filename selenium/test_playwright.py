import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_playwright_page(driver):
    driver.get("https://www.playwright.dev")
    myElement = driver.find_element(By.TAG_NAME, "h1")
    print(f"Element text is: {myElement.text}")
    myElement = driver.find_elements(By.TAG_NAME, "h1")
    print(f"Element text is: {myElement[0].text}")




def test_pw_css(driver):
    driver.set_window_size(800, 800)          # below Docusaurus's 997px breakpoint
    driver.get("https://www.playwright.dev")


    button = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Toggle navigation bar"]')
    button.click()
    
    # cliLink = driver.find_element(By.XPATH, '//*[@class=".theme-layout-navbar.navbar.navbar--fixed-top"]/div[3]/div[2]/div[1]/ul/li[3]/a')
    cliLink = driver.find_element(By.XPATH, '//*[@id="__docusaurus"]/nav/div[3]/div[2]/div[1]/ul/li[3]/a')

    print("Is displayed:", cliLink.is_displayed())
    print("Is enabled:", cliLink.is_enabled())
    print("Link text:", cliLink.text)
    print("Link href:", cliLink.get_attribute("href"))

    # cliLink = driver.find_element(By.XPATH, '/html/body/div[1]/nav/div[3]/div[2]/div[1]/ul/li[3]/a')
    cliLink.click()
    WebDriverWait(driver, 10).until(EC.url_to_be("https://playwright.dev/agent-cli/introduction"))
    assert driver.current_url == "https://playwright.dev/agent-cli/introduction"