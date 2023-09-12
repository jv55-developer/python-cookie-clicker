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

store = driver.find_elements(By.CSS_SELECTOR, value="#store div")
cookie = driver.find_element(By.CSS_SELECTOR, value="#cookie")

click_cookie = True
start_time = int(time.time())
while click_cookie:
    money = int(driver.find_element(By.ID, value="money").text)
    cookie.click()

    if int(time.time()) == start_time + 5:

        for store_item in store[:-1]:
            item = store_item.find_element(By.TAG_NAME, value="b").text
            item_value = int((item.split("- ")[1]).replace(",", ""))
            print(item_value)

            if money > item_value:
                store_item.click()

        start_time = int(time.time())

