from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_start():
    """ Start up python Selenium"""
    driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # implicit wait for Chrome
    driver.implicitly_wait(10) # default wait 0 we set industries standard timeout 10 Seconds
    driver.get('http://localhost:3000')
    # maximize_window implementation
    driver.maximize_window()
    driver.find_element(By.CSS_SELECTOR,'#username').send_keys('Katharina_Bernier')
    driver.find_element(By.CSS_SELECTOR,'#password').send_keys('s3cret')
    driver.refresh()
    time.sleep(2)
    driver.close()