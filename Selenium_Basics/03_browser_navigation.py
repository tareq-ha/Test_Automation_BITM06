import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://google.com")
time.sleep(3)

driver.get("https://apple.com")
time.sleep(3)

driver.back()
time.sleep(3)

driver.forward()
time.sleep(3)

driver.refresh()
time.sleep(3)


driver.quit()
