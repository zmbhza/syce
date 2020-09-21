import requests
import json
import xlrd
from email.mime.text import MIMEText
import smtplib
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
    def excel(self):
        wb = xlrd.open_workbook('C:\\Users\\zhao\\Desktop\\xiugai.xls')  # 打开Excel文件
        sheet = wb.sheet_by_name('becks')  # 通过excel表格名称(rank)获取工作表 #创建空list
        # 订单编号
        global s
        s = sheet.cell(1, 0).value
        # 订单金额
        global b
        b = sheet.cell(1, 1).value
    def jk(self):
        try:
            url = "https://admin.zhaolaobao.com/api/order/orderManager/modifyOrderPrice"
            payload = {
                "id":'2007',
                "totalDiscount":'0',
                "freight":'0',
                "remark":"",
                "modifyOrderDetailPriceDTOS":[
                    {
                        "id":'25142',
                        "productId":'20200630712',
                        "modifyPrice":b
                    }
                ]
            }
            headers = {
              'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mbyI6IntcImlkXCI6MTE4NyxcImNvbXBhbnlJZFwiOjcyNCxcInVzZXJuYW1lXCI6XCJUZXN0XCIsXCJwaG9uZVwiOlwiMTg4ODg4ODg4ODhcIixcInR5cGVcIjpudWxsLFwiY29kZVwiOm51bGwsXCJjb21wYW55TmFtZVwiOm51bGwsXCJsZXZlbFwiOm51bGwsXCJzYWFzRXhwaXJhdGlvblRpbWVcIjpudWxsLFwiZXhwaXJlRmxhZ1wiOm51bGwsXCJzZXJ2aWNlQ29tcGFueUlkXCI6bnVsbCxcIm9wZW5JZFwiOm51bGwsXCJpc0xvZ2luXCI6bnVsbCxcIm9yZ2FuaXphdGlvbklkXCI6bnVsbCxcInBlcm1pc3Npb25zXCI6bnVsbCxcInNlcnZpY2VDb21wYW55TmFtZVwiOm51bGx9IiwiY29kZSI6MjAwLCJ1c2VyX25hbWUiOiIxODg4ODg4ODg4ODcyNGFkbWluLnpoYW9sYW9iYW8uY29tMSIsInNjb3BlIjpbIndlYmFwcCJdLCJleHAiOjE1OTg4ODU3OTYsImF1dGhvcml0aWVzIjpbIjMyMCJdLCJqdGkiOiJmMmUyNDhjZi1mODIzLTQ4ODMtODcxYy1mZTRlNTI5OGQ0OGEiLCJjbGllbnRfaWQiOiJ6aGFvbGFvYmFvIn0.VEDJlSbdsw2BmBC_rLxUcfrnqRuBEtGh5BtNWt9xzM0',
              'Content-Type': 'application/json',
              'Cookie': 'shareSessionId=C092BAA0679371F85DDAA6064D8F309A; JSESSIONID=3703D65FB6385021E5000732F747A2AF'
            }

            response = requests.request("POST", url, headers=headers, data = json.dumps(payload))
            print(response.text)
            self.email('订单号为：' + s + '的订单价格修改成功')
        except :
            self.email('订单号为:' + s + '的订单价格修改失败')

if __name__ == '__main__':
    run().excel()
    run().jk()