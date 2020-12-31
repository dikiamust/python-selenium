# MENGOTOMATISASIKAN LOG IN INSTAGRAM / AUTOMATE LOG IN INSTAGRAM
import os
from selenium import webdriver
import time
#from confidential import userName, password (BUAT CONFIDENTIAL.PY UNTUK MENYIMPAN USERNAME & PASSWORD
#from confidential import userName, password (MAKE A CONFIDENTIAL.PY TO SAVE YOUR USERNAME & PASSWORD

driver = webdriver.Chrome (executable_path=os.path.abspath("chromedriver"))
time.sleep(1)

driver.get('https://www.instagram.com')
time.sleep(1)

driver.find_element_by_name('username').send_keys(userName)
driver.find_element_by_name('password').send_keys(password)

driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]').click()


