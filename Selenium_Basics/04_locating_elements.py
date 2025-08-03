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

customer_registration_hack_home = driver.find_element(By.CSS_SELECTOR,"form[id='customerRegisterForm'] button[type='button']")
customer_registration_hack_home.click()

customer_login_button = driver.find_element(By.CSS_SELECTOR,"#homeLoginCustomerBtnMain")
customer_login_button.click()

# Ligin
customer_login_email = driver.find_element(By.CSS_SELECTOR,"#loginEmail")
customer_login_email.send_keys("tareq@tareq.com")

customer_login_passwd = driver.find_element(By.CSS_SELECTOR,"#loginPassword")
customer_login_passwd.send_keys("123456")

customer_login_submit_button = driver.find_element(By.CSS_SELECTOR,"form[id='loginForm'] button[type='submit']")
customer_login_submit_button.click()


time.sleep(2)

customer_account_id_span = driver.find_element(By.CSS_SELECTOR,"#customerAccountIdDisplay")
customer_account_id = customer_account_id_span.text

# Deposit Funds

customer_deposit_amount = driver.find_element(By.CSS_SELECTOR,"#depositAmount")
customer_deposit_amount.send_keys("10000")

customer_deposit_submit_button = driver.find_element(By.CSS_SELECTOR,"form[id='depositForm'] button[type='submit']")
customer_deposit_submit_button.click()

time.sleep(5)

# Transaction Statement

customer_statement_datatab_button = driver.find_element(By.CSS_SELECTOR,"span[data-tab='statement']")
customer_statement_datatab_button.click()
time.sleep(5)

# Withdraw Funds

customer_withdraw_datatab_button = driver.find_element(By.CSS_SELECTOR,"span[data-tab='withdraw']")
customer_withdraw_datatab_button.click()

customer_withdraw_amount = driver.find_element(By.CSS_SELECTOR,"#withdrawAmount")
customer_withdraw_amount.send_keys("10000")

customer_withdraw_submit_button = driver.find_element(By.CSS_SELECTOR,"form[id='withdrawForm'] button[type='submit']")
customer_withdraw_submit_button.click()

time.sleep(5)

# Transaction Statement

customer_statement_datatab_button = driver.find_element(By.CSS_SELECTOR,"span[data-tab='statement']")
customer_statement_datatab_button.click()
time.sleep(5)


# Funds Transfer

customer_fund_transfer_datatab_button = driver.find_element(By.CSS_SELECTOR,"span[data-tab='transfer']")
customer_fund_transfer_datatab_button.click()

customer_recipient_account_id = driver.find_element(By.CSS_SELECTOR,"#recipientAccountId")
customer_recipient_account_id.send_keys(customer_account_id)

customer_transfer_amount = driver.find_element(By.CSS_SELECTOR,"#transferAmount")
customer_transfer_amount.send_keys("5000")

time.sleep(5)
customer_fund_transfer_submit_button = driver.find_element(By.CSS_SELECTOR,"form[id='transferForm'] button[type='submit']")
customer_fund_transfer_submit_button.click()

time.sleep(5)



# Transaction Statement

customer_statement_datatab_button = driver.find_element(By.CSS_SELECTOR,"span[data-tab='statement']")
customer_statement_datatab_button.click()
time.sleep(5)


# Logout

customer_logout_button = driver.find_element(By.CSS_SELECTOR,"#logoutButton")
customer_logout_button.click()
time.sleep(5)

