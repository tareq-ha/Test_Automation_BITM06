import time
from pkgutil import extend_path
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://muntasir101.github.io/Modern-Bank-Portal/")

# # Locating Elements
# technique:
# 1. ID (1)
# 2. NAME (2)
# 3. TAG NAME
# 4. Class Name
# 5. Link Text
# 6. Partial Link Text
# 7. CSS (3)
# 8. XPATH

time.sleep(3)

customer_registration_button = driver.find_element(By.CSS_SELECTOR,"#homeRegisterCustomerBtnMain")
customer_registration_button.click()

time.sleep(3)

customer_registration_full_name = driver.find_element(By.CSS_SELECTOR,"#customerNameReg")
customer_registration_full_name.send_keys("Tareq Hassan")

customer_registration_email = driver.find_element(By.CSS_SELECTOR,"#customerEmailReg")
customer_registration_email.send_keys("tareq@tareq.com")

customer_registration_passwd = driver.find_element(By.CSS_SELECTOR,"#customerPasswordReg")
customer_registration_passwd.send_keys("123456")

customer_registration_initial_deposit = driver.find_element(By.CSS_SELECTOR,"#initialDepositReg")
customer_registration_initial_deposit.send_keys("20000")

customer_registration_submit_button = driver.find_element(By.CSS_SELECTOR,"form[id='customerRegisterForm'] button[type='submit']")
customer_registration_submit_button.click()

time.sleep(5)



