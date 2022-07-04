from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import wget

PATH = "C:/Users/卓仕恩/OneDrive/桌面/chromedriver_win32/chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://unsplash.com/")



# WebDriverWait(driver, 10).until(
#          EC.presence_of_element_located((By.NAME, "username"))
#      )

# WebDriverWait(driver, 10).until(
#          EC.presence_of_element_located((By.NAME, "password"))
#      )
# username = driver.find_element(By.NAME, "username")
# username.clear()

# password = driver.find_element(By.NAME, "password")
# password.clear()
# login = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]')

# username.send_keys('matthewcho1234@gmail.com')
# password.send_keys('14251211abcd')
# login.click()

keyword = "anime"
search = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[1]/div/div[2]/div/div[1]/div/div/div/div[2]/div[1]/form/div[1]/input')
search.send_keys(keyword)
time.sleep(1)
search.send_keys(Keys.RETURN)
WebDriverWait(driver, 10).until(
     EC.presence_of_element_located((By.CLASS_NAME, "YVj9w"))
     )



load_more = driver.find_element(By.CLASS_NAME, "CwMIr")
time.sleep(1)
load_more.click()
time.sleep(1)

for i in range(10):
       driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
       time.sleep(1)

imgs = driver.find_elements(By.CLASS_NAME, "YVj9w")


path = os.path.join(keyword)
os.mkdir(path)

count = 0
for img in imgs:
     save_as = os.path.join(path, keyword + str(count) + '.jpg')
     if img.get_attribute("src") == None:
         continue
     print(img.get_attribute("src"))
     wget.download(img.get_attribute("src"), save_as)
     count += 1










