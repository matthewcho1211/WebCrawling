from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as Soup
import time

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

soup = Soup(driver.page_source,"lxml")
titles = soup.find_all(class_="sc-417133b6-3")
for title in titles:
    print(title.text)

