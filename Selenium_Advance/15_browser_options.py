import logging
from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Setup lgging
logging.basicConfig(
    filename = "logs/15_browser_optiona.log",
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s'
)

# initiate Chrome Options
chrome_options = Options()

# Headless option
# chrome_options.add_argument("--headless=new")
# logging.info("Setting Chrome options to HEADLESS")
chrome_options.add_argument("--headed=new")
logging.info("Setting Chrome options to HEADed")
chrome_options.add_argument("--width=700")
logging.info("Setting Chrome options width=700px")
chrome_options.add_argument("--height=600")
logging.info("Setting Chrome options height=600px")

# browser launch in incognito
chrome_options.add_argument("--private")
logging.info("Browser in Incognito")

# driver = webdriver.Chrome()
# logging.info("Browser Launch Successfully.")

logging.info("Staring Browser Session...")
driver = webdriver.Chrome(options=chrome_options)

logging.info("Browser Launch Successfully.")

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
    # logging.error("Element 'JS Prompt Alert Button' not found with Explicit wait.")
    logging.error(e)

logging.info("Script execution ends....\n\n============================================================\n")

driver.quit()
