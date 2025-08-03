import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

# goto URL
driver.get("https://muntasir101.github.io/Movie-Ticket-Booking/")

# Select from Ticket Class
try:
    ticket_class_dropdown_element =driver.find_element(By.CSS_SELECTOR,"#price")
    # ticket_class_dropdown_element =EC.presence_of_element_located(By.CSS_SELECTOR,"#price")
    select_ticket_class = Select(ticket_class_dropdown_element)

    print("Ticket Class dropdown options")
    actual_price_options = []
    for dw_options in select_ticket_class.options:
        print(dw_options.text)
        actual_price_options.append(dw_options.text)
    print(actual_price_options)
    expected_options = ['Regular - $500', 'Silver - $750', 'Gold - $1000', 'Platinum - $1500', 'VIP - $2000']
    if actual_price_options == expected_options :
        print("Ticket Class Dropdown have all option available")
    else:
        print("Ticket Class Dropdown DO NOT have all option available")

    select_ticket_class.select_by_value("750")
except Exception as e:
    print(e)


# Select is register
try:
    wait = WebDriverWait(driver, 20)
    is_register_dropdown_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#user")))
    select_is_register = Select(is_register_dropdown_element)


    print("'Are you a registered user?' dropdown options")
    actual_register_options = []
    for reg_options in select_is_register.options:
        print(reg_options.text)
        actual_register_options.append(reg_options.text)
    print("actual_register_options")
    print(actual_register_options)
    expected_register_options = ['Yes', 'No']
    if actual_register_options == expected_register_options :
        print("User Registration Status Dropdown have all option available")
    else:
        print("User Registration Status Dropdown DO NOT have all option available")

    select_is_register.select_by_value("no")
except Exception as e:
    print(e)






time.sleep(5)