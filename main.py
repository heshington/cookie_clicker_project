import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

URL = "http://orteil.dashnet.org/experiments/cookie/"
chrome_driver_path = "/Users/hirenpatel/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(URL)
# check every 5 seconds to see which upgrades you can get, pick the most expensive one

time_str = "%M"


def start_game(time_started):
    stop = time_started + datetime.timedelta(minutes=1)
    money = driver.find_elements_by_id("money")
    store = driver.find_elements_by_id("store")
    print(type(store))
    time_last_checked = datetime.datetime.now()
    #Loop that runs for 5min
    while datetime.datetime.now() < stop:
        #Click the cookie
        cookie = driver.find_element_by_id("cookie")
        cookie.click()
        #every 5 seconds check the store to see if you can buy something.
        if datetime.datetime.now() > (time_last_checked + datetime.timedelta(seconds=5)):
            # Check for the most expensive thing in the store that you can afford.
            for item in store:
                cost = driver.find_element_by_css_selector(f"{item.tag_name} moni")
                print(item.get_attribute("id"))




start_game(datetime.datetime.now())
