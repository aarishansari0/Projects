from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

keyword = input("Enter what you want to find on wiki:\n")
PATH="chromedriver.exe"
c_service=webdriver.ChromeService(executable_path=PATH)
driver=webdriver.Chrome(service=c_service)
driver.get("https://wikipedia.org")
driver.maximize_window()
WebDriverWait(driver, 5).until(
    ec.element_to_be_clickable((By.ID,"searchInput"))
    )
inp = driver.find_element(By.ID,"searchInput")
inp.send_keys(keyword+Keys.ENTER)

time.sleep(10)
driver.quit()