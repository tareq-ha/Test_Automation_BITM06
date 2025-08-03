import logging
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup lgging
logging.basicConfig(
    filename = "logs/13_log.log",
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("Starting Browser Session")

driver = webdriver.Chrome()
logging.info("Browser Launch Successfully.")

driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
logging.info("URL Open Successfully.")

try:
    wait = WebDriverWait(driver, 20)
    js_alert = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[onclick='jsAlert()']")))
    js_alert.click()
    logging.info("Click on JS Normal Alert")
    js_alert_title = driver.switch_to.alert.text
    logging.info(js_alert_title)
    driver.switch_to.alert.accept() # click on ok
    logging.info("Alert Accept.")
except Exception as e:
    logging.error("Element 'JS Alert Button' not found with Explicit wait.")

try:
    wait = WebDriverWait(driver, 20)
    js_confirm_alert = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[onclick='jsConfirm()']")))
    js_confirm_alert.click()
    logging.info("Click on JS Confirm Alert")
    confirm_alert_title = driver.switch_to.alert.text
    logging.info(confirm_alert_title)
    driver.switch_to.alert.dismiss() # click on Cancel
    logging.info("Alert Canceled.")
except Exception as e:
    logging.error("Element 'JS Confirm Alert Button' not found with Explicit wait.")

try:
    wait = WebDriverWait(driver, 20)
    js_prompt_alert = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[onclick='jsPrompt()']")))
    js_prompt_alert.click()
    logging.info("Click on JS Prompt Alert")
    confirm_prompt_alert_title = driver.switch_to.alert.text
    logging.info(confirm_prompt_alert_title)
    driver.switch_to.alert.send_keys("Test Text")
    driver.switch_to.alert.accept()
    logging.info("Alert Accepted.")
except Exception as e:
    logging.error("Element 'JS Prompt Alert Button' not found with Explicit wait.")

driver.quit()