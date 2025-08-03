import logging
from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# Setup logging
logging.basicConfig(
    filename = "logs/17_downloads.log",
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s'
)

# Set download directory
download_dir = os.path.abspath("assets/downloads")
if not os.path.exists(download_dir)
    os.makedirs(download_dir)

# initiate Chrome Options
chrome_options = Options()

# initialize Firefox Options
chrome_options = Options()
chrome_options.set_preference("browser.download.folderList",2)
chrome_options.set_preference("browser.download.dir", download_dir)
chrome_options.set_preference("browser.helperApps.neverAsk.saveToDisk","text/plain,application/pdf")
chrome_options.set_preference("browser.download.manager.showWhenStarting", False)

# Headless option
# chrome_options.add_argument("--headless=new")
# logging.info("Setting Chrome options to HEADLESS")
# chrome_options.add_argument("--headed=new")
# logging.info("Setting Chrome options to HEADed")
# chrome_options.add_argument("--width=700")
# logging.info("Setting Chrome options width=700px")
# chrome_options.add_argument("--height=600")
# logging.info("Setting Chrome options height=600px")
#
# # browser launch in incognito
# chrome_options.add_argument("--private")
# logging.info("Browser in Incognito")

# driver = webdriver.Chrome()
# logging.info("Browser Launch Successfully.")

logging.info("Staring Browser Session...")
driver = webdriver.Chrome(options=chrome_options)

logging.info("Browser Launch Successfully.")

driver.implicitly_wait(5)

logging.info("Browser Launch Successfully.")

driver.implicitly_wait(5)

driver.get("https://github.com/Muntasir101/Test_Automation_BITM06/blob/master/Selenium_Advance/logs/13_log.log")
logging.info("URL Open Successfully.")

driver.find_element(By.CSS_SELECTOR, ".octicon.octicon-download[aria-hidden='true'][focusable='false']").click()
logging.info("File Download successfully.")

logging.info("Script Complete.")

driver.quit()

logging.info("End Browser Session...")