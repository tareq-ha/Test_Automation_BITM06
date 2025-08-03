import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(5)

# goto URL
driver.get("https://epassport.gov.bd/onboarding")

# Click Not Bangladeshi
try:
    no_bangladeshi =driver.find_element(By.CSS_SELECTOR,"label[for='applying-bangladeshCommon.Labels.No']")
    no_bangladeshi.click()
except Exception as e:
    print(e)
time.sleep(2)

# Click Bangladeshi Yes
try:
    wait = WebDriverWait(driver,20)
    yes_bangladeshi =driver.find_element(By.CSS_SELECTOR,"label[for='applying-bangladeshCommon.Labels.Yes']")
    yes_bangladeshi.click()
except Exception as e:
    print(e)
time.sleep(2)


# Select District
try:
    wait = WebDriverWait(driver, 20)
    district =wait.until(EC.presence_of_element_located((By.XPATH,"(//input[@type='text'])[1]")) )
    district.click()
    district.send_keys("Dhaka")
    time.sleep(2)
    district.send_keys(Keys.ARROW_DOWN)
    district.send_keys(Keys.ENTER)
    time.sleep(2)

    # print(district_dropdown_element)
    # //yes_bangladeshi.click()
except Exception as e:
    print(e)
# time.sleep(2)

# Select police station
try:
    wait = WebDriverWait(driver, 20)
    # policeStation =wait.until(EC.presence_of_element_located((By.XPATH,"/html[1]/body[1]/vbeop-root[1]/div[1]/div[2]/vbeop-onboarding[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[3]/div[1]/vbeop-select[1]/div[2]/ng-select[1]/div[1]/div[1]/div[2]/input[1]")) )
    policeStation =wait.until(EC.presence_of_element_located((By.XPATH,"(//input[@type='text'])[2]")) )
    policeStation.click()
    policeStation.send_keys("BADDA")
    time.sleep(2)
    policeStation.send_keys(Keys.ARROW_DOWN)
    policeStation.send_keys(Keys.ENTER)
    time.sleep(5)

    # print(district_dropdown_element)
    # //yes_bangladeshi.click()
except Exception as e:
    print(e)
# time.sleep(2)

