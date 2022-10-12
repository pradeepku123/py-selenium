from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def test_app_command_explore():
    """ This Method Where We Explore application Commands"""
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('http://localhost:3000')
    driver.maximize_window()
    
    # Get Title of Current Web Page
    print(driver.title)
    
    # Get Current URL
    print(driver.current_url)

    # Get Page Source Code
    # print(driver.page_source)
    
    # Conditional Method
    
    print(driver.find_element(By.CSS_SELECTOR,'#username').is_enabled())
    print(driver.find_element(By.CSS_SELECTOR,'#username').is_displayed())
    
    driver.quit()