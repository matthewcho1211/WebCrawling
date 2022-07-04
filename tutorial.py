from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup as Soup

PATH = "C:/Users/卓仕恩/OneDrive/桌面/chromedriver_win32/chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://www.dcard.tw/f")
print(driver.title)
search = driver.find_element(By.NAME, "query")
search.clear()
search.send_keys("輔仁大學")
search.send_keys(Keys.RETURN)


WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "sc-f860e6e9-1"))
    )

for i in range(10):
       driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
       time.sleep(1)


titles = driver.find_elements(By.CLASS_NAME, "sc-417133b6-3")
for title in titles:
    print(title.text)












