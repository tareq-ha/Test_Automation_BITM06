from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

driver.implicitly_wait(10)

driver.get("https://google.com")

try:
    driver.save_screenshot("assets/images/Google.png")
    print("Screenshot capture successful")
except Exception as e:
    print(e)


driver.quit()