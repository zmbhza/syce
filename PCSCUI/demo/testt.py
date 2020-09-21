from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import time
import pymysql
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
# driver = webdriver.Chrome(r"E:\guge\chromedriver.exe")
# driver.maximize_window()
# time.sleep(2)
# driver.get('http://admin.bsapo.com/')
# time.sleep(5)
# driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/div[1]/input').send_keys('17611520838')
# driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/div[2]/input').send_keys('a123456')
# driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/button').click()
# time.sleep(2)
# driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/ul/li[2]/div').click()
# time.sleep(2)
# driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/ul/li[2]/ul/li').click()
# time.sleep(3)
# driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[4]/table/tbody[1]/tr[2]/td[12]/a[2]').click()
# time.sleep(1.5)
#
# js='''document.getElementsByClassName("ivu-input ivu-input-default ivu-input-with-suffix")[1].removeAttribute("readonly");
#         document.getElementsByClassName("ivu-input ivu-input-default ivu-input-with-suffix")[1].value="2020-08-27";'''
# driver.execute_script(js)
# driver.find_elements_by_class_name("ivu-input ivu-input-default ivu-input-with-suffix")
# driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/div/div[3]/p/span[1]').click()



def sql_select(aa,bb):
    s = pymysql.connect(
        host="47.111.103.72",  # 数据库地址
        port=26535,  # 端口号
        db='qs_3.0_product',  # 数据库名
        user="root",  # 用户名
        passwd="WYmjdijDldsiqnporelease",  # 密码
        charset="utf8",  # 指定字符编码
    )
    c = s.cursor()
    sq = "SELECT id FROM tb_product_cash_sale WHERE id like %s  LIMIT 1"  # 2、读user表的数据
    c.execute(sq,aa)   # 执行sql语句
    ((row,),) = c.fetchall()    # 全部读出来
    print(row)
    if bb == (row):
            print('查询到新增数据')
    else:
            print('未查询到对应的数据') #删除库中信息后可报此错误

    c.close() #关闭数据库链接
sql_select(16899,16899)