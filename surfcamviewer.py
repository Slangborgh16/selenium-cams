from time import sleep

from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox('./rg2vxw1g.adblocker')

driver.get("https://www.surfguru.com/rcs-satellite-beach-surf-report")
assert "Satellite Beach" in driver.title

sleep(5)
player = WebDriverWait(driver, 20).until(
     EC.element_to_be_clickable((By.XPATH, '//*[@id="player"]'))
     )
player.click()
player.send_keys("f")
