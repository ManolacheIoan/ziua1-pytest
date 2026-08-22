from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def test_login_success():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://the-internet.herokuapp.com/login")

    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")
    username.send_keys("tomsmith")
    password.send_keys("SuperSecretPassword!")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    success_message = driver.find_element(By.CSS_SELECTOR, ".flash.success")
    assert "You logged into a secure area" in success_message.text

    driver.quit()


def test_login_failure():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://the-internet.herokuapp.com/login")

    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")
    username.send_keys("wronguser")
    password.send_keys("wrongpass")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    error_message = driver.find_element(By.CSS_SELECTOR, ".flash.error")
    assert "Your username is invalid" in error_message.text

    driver.quit()


def test_login_with_wait():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://the-internet.herokuapp.com/login")

    wait = WebDriverWait(driver, 10)
    username = wait.until(EC.presence_of_element_located((By.ID, "username")))
    username.send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    success = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".flash.success")))
    assert "secure area" in success.text

    driver.quit()

    from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_with_wait():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://the-internet.herokuapp.com/login")

    wait = WebDriverWait(driver, 10)
    username = wait.until(EC.presence_of_element_located((By.ID, "username")))
    username.send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    success = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".flash.success")))
    assert "secure area" in success.text

    driver.quit()