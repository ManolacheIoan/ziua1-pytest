from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    drv = webdriver.Chrome(service=service)
    yield drv
    drv.quit()


def test_checkbox_can_be_checked(driver):
    driver.get("https://the-internet.herokuapp.com/checkboxes")
    
    checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
    
    assert len(checkboxes) == 2
    
    first_checkbox = checkboxes[0]
    assert not first_checkbox.is_selected()
    
    first_checkbox.click()
    assert first_checkbox.is_selected()


def test_second_checkbox_starts_checked(driver):
    driver.get("https://the-internet.herokuapp.com/checkboxes")
    
    checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
    second_checkbox = checkboxes[1]
    
    assert second_checkbox.is_selected()
