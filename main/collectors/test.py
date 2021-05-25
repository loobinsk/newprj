from selenium import webdriver
import os
from time import sleep

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(executable_path="./chromedriver", options=chrome_options)
driver.get('https://www.google.com')
sleep(10)
driver.quit()
