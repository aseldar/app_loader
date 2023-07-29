import time
import random
import glob
import os


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from flask import Flask, request, render_template, send_from_directory

# create the Flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

useragent = UserAgent()
chrome_driver_path = f"/usr/local/bin/chromedriver"

@app.route('/get_price', methods=['POST'])
def get_price():
    latest_file = loader()
    print(f"load is done: {latest_file}")
    return send_from_directory('', latest_file, as_attachment=True)

def loader():
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
    username.send_keys("Innodata")
    password.send_keys("Parol123")
    driver.find_element(By.NAME, "Login").click()
    time.sleep(random.randint(1,5))
    
    driver.get("https://www.dkc.ru/ru/personal/price/")
    time.sleep(random.randint(5,10))

    button = driver.find_element(By.CLASS_NAME, "downloadSection__link")
    driver.execute_script("arguments[0].click();", button)

    # driver.find_element(By.CLASS_NAME, "downloadSection__link").click()
    # driver.find_element(By.XPATH, """//*[@id="documents9130"]/ul/li/a""").click()
    time.sleep(random.randint(1,5))
    driver.quit()

    list_of_files = glob.glob('*.zip') 
    latest_file = max(list_of_files, key=os.path.getctime)
    print(latest_file)
    
    return latest_file


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
    
    # try:
    #     loader()
    # except Exception as e:

    #     print('Произошла ошибка', e)
