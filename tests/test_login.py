import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utils.config import USERNAME, PASSWORD, DOMAIN



@pytest.fixture
def driver():
    driver = webdriver.Chrome()  # ChromeDriver kurulu olmalı
    yield driver
    driver.quit()


def test_kraken_login(driver):
    driver.get(DOMAIN)

    # Login sayfasına git
    login_button = driver.find_element(By.LINK_TEXT, "Log in")  # Örneğin: "Sign In" düğmesi
    login_button.click()
    driver.implicitly_wait(5)

    # Kullanıcı bilgilerini gir
    driver.find_element(By.XPATH, "//*[@name = 'username']").send_keys(USERNAME)
    driver.find_element(By.XPATH, "//*[@name = 'password']").send_keys(PASSWORD + Keys.RETURN)
    driver.find_element(By.LINK_TEXT, "Use passkey").click()
    print("Lütfen biyometrik doğrulamayı tamamlayın...")
    time.sleep(30)
    # Portföy değeri kontrolü
    portfolio_value = driver.find_element(By.XPATH, "//*[@class = 'text-ds-primary']").text  # Portföy değerinin ID'si örnektir
    assert portfolio_value is not None
