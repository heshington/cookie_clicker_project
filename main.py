import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re

URL = "http://orteil.dashnet.org/experiments/cookie/"
# chrome_driver_path = "/Users/hirenpatel/Development/chromedriver"
chrome_driver_path = "/home/hiren/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(URL)
# check every 5 seconds to see which upgrades you can get, pick the most expensive one



store_items = {}



#Get upgrade item ids.
items = driver.find_elements_by_css_selector("#store div")
item_ids = [item.get_attribute("id") for item in items]

def get_item_cost(item):
    store_text = item.find_element_by_tag_name("b")
    split_store_text = store_text.text.split("-")
    item_text = split_store_text[0]
    item_cost = split_store_text[1]
    item_cost = re.sub("[^0-9]", "", item_cost)
    item_cost = item_cost.rstrip()
    item_cost = int(item_cost)
    item_text = item_text.rstrip()
    store_items[item_text] = item_cost



print(store_items)



timeout = time.time() + 5
five_min =  time.time() + 60 + 5
while True:

    buyCursor = driver.find_element_by_id("buyCursor")
    buyGrandma = driver.find_element_by_id("buyGrandma")
    buyFactory = driver.find_element_by_id("buyFactory")
    buyMine = driver.find_element_by_id("buyMine")
    buyShipment = driver.find_element_by_id("buyShipment")
    buy_alchemy_lab = driver.find_element_by_id("buyAlchemy lab")
    buyPortal = driver.find_element_by_id("buyPortal")
    buyTime_machine = driver.find_element_by_id("buyTime machine")
    listed_upgrades = [buyCursor, buyGrandma, buyFactory, buyMine, buyShipment, buy_alchemy_lab, buyPortal,
                       buyTime_machine]

    for item in listed_upgrades:
        get_item_cost(item)
    cookie = driver.find_element_by_id("cookie")
    cookie.click()
    if time.time() > timeout:
        # Get all upgrade <b> tags
        #all_prices = driver.find_elements_by_css_selector("#store b")
        for item in listed_upgrades:
            get_item_cost(item)
        item_prices = list(store_items.values())
        print(type(item_prices))

        # Create dictionary of store itewhims and prices
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = listed_upgrades[n]

        #get current cookie count
        money = driver.find_element_by_id("money").text
        if "," in money:
            money = money.replace(",", "")
        cookie_count = int(money)

        # Find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

                # Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element_by_id(to_purchase_id).click()

            # Add another 5 seconds until the next check
        timeout = time.time() + 5

    # After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > five_min:
        cookie_per_s = driver.find_element_by_id("cps").text
        print(cookie_per_s)
        break
