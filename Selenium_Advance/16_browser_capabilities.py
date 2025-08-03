import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# Setup lgging
logging.basicConfig(
    filename = "logs/17_download.log",
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("Starting Browser Session....")


driver = webdriver.Chrome()
logging.info("Browser Launch Successfully.")

driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://practice.expandtesting.com/upload")
logging.info("URL Open Successfully.")




logging.info("Script execution ends....\n\n============================================================\n")

driver.quit()
