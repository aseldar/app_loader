import time
import random
import glob
import os

from utils.utils import loader_dkc, loader_iek

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

# useragent = UserAgent()
# chrome_driver_path = f"/usr/local/bin/chromedriver"

@app.route('/get_price_dkc', methods=['POST'])
def get_price_dkc():
    latest_file = loader_dkc()
    print(f"load is done: {latest_file}")
    return send_from_directory('', latest_file, as_attachment=True)

@app.route('/get_price_iek', methods=['POST'])
def get_price_iek():
    latest_file = loader_iek()
    print(f"load is done: {latest_file}")
    return send_from_directory('', latest_file, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)