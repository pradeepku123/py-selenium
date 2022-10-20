from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_start():
    """ Start up python Selenium"""
    driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('http://localhost:3000')
    driver.find_element(By.CSS_SELECTOR,'#username').send_keys('Katharina_Bernier')
    driver.find_element(By.CSS_SELECTOR,'#password').send_keys('s3cret')
    driver.refresh()
    time.sleep(2)
    driver.close()