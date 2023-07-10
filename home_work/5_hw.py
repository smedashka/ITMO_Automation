from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


def find_elements():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    try:
        driver.find_element(By.CSS_SELECTOR, '#user-name')
        driver.find_element(By.CSS_SELECTOR, '#passwordd')
        driver.find_element(By.CSS_SELECTOR, '#login-button')
    except NoSuchElementException:
        pass
    print('Элементы найдены')


find_elements()

