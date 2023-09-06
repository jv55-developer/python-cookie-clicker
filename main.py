from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Keep Chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# Open site
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.CSS_SELECTOR, value="#cookie")

store = driver.find_elements(By.CSS_SELECTOR, value="#store div")
print(type(store))

# click_cookie = True
# start_time = int(time.time())
# while click_cookie:
#
#     cookie.click()
#
#     if int(time.time()) == start_time + 5:
#
#         start_time = int(time.time())
