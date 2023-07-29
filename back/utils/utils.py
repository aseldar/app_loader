import time
import random
import glob
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent

useragent = UserAgent()

def loader_iek():
    options = Options()
    # options.headless = True
    options.add_argument(f'user-agent={useragent.random}')
    options.add_argument('---incognito')
    options.add_argument('---disable-extension')
    options.add_argument("--no-sandbox")
    options.add_argument('--disable-gpu')
    options.add_argument('--headless')

    driver = webdriver.Chrome(options=options) 
    driver.get('https://www.iek.ru/products/price/')
    driver.find_element(By.NAME, "submit").click()
    time.sleep(5)
    driver.quit()

    list_of_files = glob.glob('*.zip') 
    latest_file = max(list_of_files, key=os.path.getctime)
    print(latest_file)
    
    return latest_file


def loader_dkc():
    options = Options()
    # options.headless = True
    options.add_argument(f'user-agent={useragent.random}')
    options.add_argument('---incognito')
    options.add_argument('---disable-extension')
    options.add_argument("--no-sandbox")
    options.add_argument('--disable-gpu')
    options.add_argument('--headless')

    driver = webdriver.Chrome(options=options)  

    driver.get("https://www.dkc.ru/ru/auth/")
    time.sleep(random.randint(1,5))
    username = driver.find_element(By.NAME, "USER_LOGIN")
    password = driver.find_element(By.NAME, "USER_PASSWORD")

    username.send_keys(os.environ.get('DKC_USER'))
    password.send_keys(os.environ.get('DKC_PASSWORD'))

    driver.find_element(By.NAME, "Login").click()
    time.sleep(random.randint(1,5))
    
    driver.get("https://www.dkc.ru/ru/personal/price/")
    time.sleep(random.randint(5,10))

    button = driver.find_element(By.CLASS_NAME, "downloadSection__link")
    driver.execute_script("arguments[0].click();", button)

    time.sleep(random.randint(5,10))
    driver.quit()

    list_of_files = glob.glob('*.zip') 
    latest_file = max(list_of_files, key=os.path.getctime)
    print(latest_file)
    
    return latest_file