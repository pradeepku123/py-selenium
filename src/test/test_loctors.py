from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
def test_explore_locators():
    """ Explore Selenium Locator"""
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('http://localhost:3000')
    driver.maximize_window() # maximize Browser Window
    # Explore ID
    driver.find_element(By.ID,'username')
    
    # Explore Name
    driver.find_element(By.NAME,'username')
    
    # Explore Find_elements
    input_ele=driver.find_elements(By.CSS_SELECTOR,'.MuiOutlinedInput-input')
    print(input_ele,len(input_ele))
    time.sleep(3)
    
    driver.close()
    