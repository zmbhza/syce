from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import time
import pyautogui
from demo import params
# 实例化Options对象
# chrome_options = Options()
# # 增加一个参数, 告诉浏览器是无头浏览器
# chrome_options.add_argument('--headless')
# # 增加一个参数, 告诉浏览器不需要使用GPU渲染
# chrome_options.add_argument('--disable-gpu')
# path = (r"E:\guge\chromedriver.exe")
# driver = webdriver.Chrome(executable_path=path, options=chrome_options)
driver = webdriver.Chrome(r"E:\guge\chromedriver.exe")
driver.maximize_window()
time.sleep(2)
driver.get('https://tq.bsapo.com/')
time.sleep(5)
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div[1]/div[2]/div/div[2]/button[2]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="app"]/div[6]/div[2]/div[4]/form[1]/div[1]/div/div[2]/input').send_keys('17611520838')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="app"]/div[6]/div[2]/div[4]/form[1]/div[2]/div/div/input').send_keys('a123456')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="app"]/div[6]/div[2]/div[4]/div[2]').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="app"]/div[3]/div/div[1]/div[2]/ul/li[1]/span/a').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="searchBox"]/span').click()
time.sleep(5)
params.handles(driver)
driver.find_element_by_xpath('//*[@id="searchBox"]/div/input').send_keys('asd')
params.mouse_move(driver,'//*[@id="covered2"]/div[1]/div[2]/div[2]/div[1]/img')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="covered2"]/div[1]/div[2]/div[2]/div[1]/div[4]').click()
params.takeScreenshot(driver,params.createDir(),'购物车')
print(driver.find_element_by_xpath('//*[@id="allinput"]/h3/div/div[3]/table/tbody/tr/td[2]/div/span').text)
js = "document.getElementsByClassName('ivu-input ivu-input-default ivu-input-with-suffix')[0].click();" \
           "document.getElementsByClassName('ant-select-search__field')[0].value='2020-08-27'"
driver.execute_script(js)
