from selenium import webdriver
import os
import time
iedriver = r"E:\guge\chromedriver.exe"
#os.environ["webdriver.ie.driver"] = iedriver
driver = webdriver.Chrome(iedriver)
driver.maximize_window()
time.sleep(2)
driver.get("https://admin.zhaolaobao.com")
time.sleep(2)
#driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/div[1]/input').send_keys('17611520838')
time.sleep(2)
driver.quit()
