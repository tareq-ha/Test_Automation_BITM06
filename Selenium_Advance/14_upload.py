import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# Setup lgging
logging.basicConfig(
    filename = "logs/14_upload.log",
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

# try:
#     wait = WebDriverWait(driver, 20)
#     file_name = "Google_img.png"
#     file_path = os.path.abspath(os.path.join("files",file_name))
#     logging.info("File Path Set Successfully.")
#
#     choose_file_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#fileInput")))
#     choose_file_button.send_keys(file_path)
#     logging.info("File Selected Successfully..")
#     time.sleep(5)
#
#     upload_button = wait.until(EC.element_to_be_clickable((By.ID, "fileSubmit")))
#     driver.execute_script("arguments[0].scrollIntoView();", upload_button)
#     upload_button.click()
#     logging.info("Upload Button Clicked Successfully..")
#
# except Exception as e:
#     logging.info(e)


try:
    wait = WebDriverWait(driver, 20)
    file_name ="SRS.docx"
    file_path = os.path.abspath(os.path.join("assets/docs", file_name))

    logging.info(file_path)


    choose_file_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#fileInput")))
    choose_file_button.send_keys(file_path)
    logging.info("File selected successfully.... ")

    upload_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#fileSubmit")))
    upload_button.click()
    logging.info("Upload button clicked successfully.... ")
except Exception as e:
    logging.error(e)

logging.info("Script execution ends....\n\n============================================================\n")

driver.quit()

