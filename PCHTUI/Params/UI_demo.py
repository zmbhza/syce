import random
from selenium import webdriver
import os,time
import pyautogui
import xlrd
from twilio.rest import Client
from email.mime.text import MIMEText
import smtplib
from selenium.webdriver.common.by import By
class run():
    def email(self,b):
        msg = MIMEText('报告')
        msg["Subject"] = b
        msg['From'] = '847160625@qq.com'
        msg['To'] = 'zhaodongshuai@zhaolaobao.com'
        fron_addr = '847160625@qq.com'
        pwd = 'bkvqmglgvrblbcai'
        smtp_server = 'smtp.qq.com'
        to_addr = 'zhaodongshuai@zhaolaobao.com'
        try:
            server = smtplib.SMTP_SSL(smtp_server, 465, timeout=2)
            server.login(fron_addr, pwd)
            server.sendmail(fron_addr, [to_addr], msg.as_string())
            server.quit()
            print('ok')
        except Exception as e:
            print('Faild:%s' % e)
    def send_msg(self,message):
        account_sid = 'AC7b56757e55dad8a593ab9350e7b7075f'
        auth_token = 'fd7c198c5e22d44558e73593945cf223'
        # 实例化
        client = Client(account_sid, auth_token)
        u'自定义短信内容message'
        msg = client.messages.create(
            to='+8617611520838',  # 要给谁发短信, 必须带区号, 中国要加上+86
            from_='+19548002273',  # 你自己twilio网站申请的手机号码, 必须带上+号
            body=message ) # 你的短信内容
    def denglu(self):
        global de
        #project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        de = webdriver.Chrome(r"E:\guge\chromedriver.exe")
        de.maximize_window()
        de.get(r"http://admin.bsapo.com/")
    def excel(self):
        wb = xlrd.open_workbook('C:\\Users\\zhao\\Desktop\\xiugai.xls')# 打开Excel文件
        sheet = wb.sheet_by_name('becks')#通过excel表格名称(rank)获取工作表 #创建空list
        #订单编号
        global s
        s = sheet.cell(1,0).value
        #订单金额
        global b
        b = sheet.cell(1,1).value
    def clear(self,b):
        de.implicitly_wait(5)
        de.find_element_by_xpath(b).clear()
    def input1(self,a,b,c):
        if c =='input':
            de.implicitly_wait(5)
            de.find_element_by_xpath(a).send_keys(b)
    def click(self,a,b):
        if b =='dianji':
            de.implicitly_wait(5)
            de.find_element_by_xpath(a).click()
    def yunxing(self):
        try :
            self.input1('//*[@id="app"]/div/div/div[2]/div[3]/div[1]/input','17611520838','input')
            self.input1('//*[@id="app"]/div/div/div[2]/div[3]/div[2]/input','a123456','input')
            self.click('//*[@id="app"]/div/div/div[2]/div[3]/button','dianji')
            self.click('//*[@id="app"]/div/div[1]/div/ul/li[2]/div','dianji')
            self.click('//*[@id="app"]/div/div[1]/div/ul/li[2]/ul/li','dianji')
            time.sleep(3)
            pyautogui.click(448,554)
            time.sleep(2)
            self.click('//*[@id="app"]/div/div[2]/div[2]/div/div[4]/table/tbody[1]/tr[2]/td[12]/a[1]','dianji')
            self.clear('//*[@id="app"]/div/div[2]/div[2]/div/div/table/tr[2]/td[7]/div/input')
            self.input1('//*[@id="app"]/div/div[2]/div[2]/div/div/table/tr[2]/td[7]/div/input',b,'input')
            self.click('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/span[1]','dianji')
            self.click('//*[@id="app"]/div/div[2]/div[2]/div/div[2]/form/div[4]/span[2]','dianji')
            self.email('订单号为：'+s+'的订单价格修改成功')
            de.quit()
        except :
            self.email('订单号为:'+s+'的订单价格修改失败')
            de.quit()
if __name__ == '__main__':
    run().denglu()
    run().excel()
    run().yunxing()