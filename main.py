from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Keep Chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# Open site
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.CSS_SELECTOR, value="#cookie")
list_of_store_items = driver.find_elements(By.CSS_SELECTOR, value="#store div")

start_time = int(time.time())
timeout = time.time() + 60*5
while True:
    money = int(driver.find_element(By.ID, value="money").text.replace(",", ""))
    cookie.click()

    list_of_store_items = driver.find_elements(By.CSS_SELECTOR, value="#store div")

    if int(time.time()) == start_time + 5:
        for store_item in list_of_store_items[:-1]:
            item = store_item.text
            item_value = int(item.split("\n")[0].split("- ")[1].replace(",", ""))

            if money > item_value:
                item_id = store_item.get_attribute("id")
                item_to_click = driver.find_element(By.ID, value=item_id)
                item_to_click.click()

        start_time = int(time.time())
