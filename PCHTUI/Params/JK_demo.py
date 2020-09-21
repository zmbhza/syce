import requests
import json,time
import xlrd
from email.mime.text import MIMEText
import smtplib
class run():
    def email(self,b,c):
        msg = MIMEText('code码返回为：'+c)
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
        except :
            print('发送邮件失败')
    def excel(self):
        wb = xlrd.open_workbook('C:\\Users\\zhao\\Desktop\\xiugai.xls')  # 打开Excel文件
        sheet = wb.sheet_by_name('becks')  # 通过excel表格名称(rank)获取工作表 #创建空list
        # 订单编号
        global s
        s = sheet.cell(1, 1).value
        # 订单金额

        global b
        b = sheet.cell(1, 1).value

    def login(self):
        try:
            url = "https://admin.zhaolaobao.com/api/uc/userFront/login/nologin"

            payload = "{\r\n    \"username\":\"18888888888\",\r\n    \"password\":\"8PTYma1PZ/g/sEKcyU+C+Q==\",\r\n    \"automatic\":\"0\",\r\n    \"source\":\"1\",\r\n    \"code\":\"\",\r\n    \"randString\":\"h8SPCpF1Xkpbdtkt\",\r\n    \"wechatCode\":\"\"\r\n}"
            headers = {
                'Content-Type': 'application/json',
                'Cookie': 'JSESSIONID=14F084FC7C5E396D273718E2729356B8; shareSessionId=14F084FC7C5E396D273718E2729356B8'
            }

            response = requests.request("POST", url, headers=headers, data=payload)
            global access_token
            access_token = response.json()["body"]["access_token"]
        except:
            self.email('账号登录失败','请查收')

    def jk(self):
        try:
            self.login(),self.excel()
            url = "https://admin.zhaolaobao.com/api/order/orderManager/modifyOrderPrice"
            payload = {
                "id":'2063',
                "totalDiscount":'0',
                "freight":'0',
                "remark":"",
                "modifyOrderDetailPriceDTOS":[
                    {
                        "id":'25203',
                        "productId":'20200630675',
                        "modifyPrice":b
                    }
                ]
            }
            headers = {
              'Authorization': 'Bearer '+ access_token,
              'Content-Type': 'application/json',
              'Cookie': 'shareSessionId=C092BAA0679371F85DDAA6064D8F309A; JSESSIONID=3703D65FB6385021E5000732F747A2AF'
            }

            response = requests.request("POST", url, headers=headers, data = json.dumps(payload))
            a = response.json()
            if a['code']==200:
                code = str(a['code'])
                self.email('订单号为：' + str(s) + '的订单价格修改成功11111111111111',code)

            else:
                code = str(a['code'])
                self.email('订单号为：' + str(s) + '的订单价格修改失败',code)
        except:
            self.email('订单号为:' + str(s) + '的订单价格修改失败','代码错误')

if __name__ == '__main__':
    run().jk()
