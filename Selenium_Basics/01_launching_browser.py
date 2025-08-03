from selenium import webdriver
import time, random


# driver = webdriver.Chrome()
# driver.maximize_window()
#
# driver.get("http://google.com")
# driver.quit()


browsers = ["Chrome", "Chrome",  "Chrome",  "Chrome",  "Chrome", "Firefox", "Edge"]
uri_list = ["https://google.com", "https://yahoo.com","https://nasa.gov", "https://prothomalo.com", "https://facebook.com"]

for browser_item in browsers:
    try:
        functionToCall=getattr(webdriver, browser_item)
        # functionToCall=getattr(webdriver, browser_item)
        # driver= functionToCall()
        driver=getattr(webdriver, browser_item)()
        driver.maximize_window()
        random_uri = random.choice(uri_list)
        driver.get(random_uri)
        time.sleep(2)
        driver.quit()
    except Exception as e:
        print("The error is: ", e)


