import requests
import xlwt
from demo import ceshi3 as ce
class test():
  def login(self):
    url = "https://admin.zhaolaobao.com/api/uc/userFront/login/nologin"

    payload = "{\r\n    \"username\":\"18888888888\",\r\n    \"password\":\"8PTYma1PZ/g/sEKcyU+C+Q==\",\r\n    \"automatic\":\"0\",\r\n    \"source\":\"1\",\r\n    \"code\":\"\",\r\n    \"randString\":\"h8SPCpF1Xkpbdtkt\",\r\n    \"wechatCode\":\"\"\r\n}"
    headers = {
        'Content-Type': 'application/json',
        'Cookie': 'JSESSIONID=14F084FC7C5E396D273718E2729356B8; shareSessionId=14F084FC7C5E396D273718E2729356B8'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    global access_token
    access_token = response.json()["body"]["access_token"]
  def down(self):
    self.login()
    url = "https://admin.zhaolaobao.com/api/order/orderManager/findOrderList"

    payload = "{\r\n    \"productName\":null,\r\n    \"brandName\":null,\r\n    \"modelName\":null,\r\n    \"payType\":null,\r\n    \"startTime\":null,\r\n    \"endTime\":null,\r\n    \"orderNumber\":null,\r\n    \"relatedOrderNumber\":null,\r\n    \"source\":null,\r\n    \"companyName\":null,\r\n    \"orderState\":2,\r\n    \"inventoryType\":null,\r\n    \"timeType\":1,\r\n    \"time\":[\r\n        \"\",\r\n        \"\"\r\n    ],\r\n    \"customerType\":null,\r\n    \"page\":1,\r\n    \"pageSize\":1000\r\n}"
    headers = {
      'Authorization': 'Bearer '+access_token,
      'Content-Type': 'application/json',
      'Cookie': 'JSESSIONID=E4ECD9050E5D627B4867156198F1F457; shareSessionId=E4ECD9050E5D627B4867156198F1F457'
    }

    response = requests.request("POST", url, headers=headers, data = payload)
    s = response.json()
    global b


    try:
      for i in range(1,10):
          global b,a
          b =  s['body']['list'][i]['orderNumber']
          a = s['body']['list'][i]['companyName']
          c = s['body']['list'][i]['id']
          o = s['body']['list'][i]['products'][0]['id']
          p = s['body']['list'][i]['products'][0]['productId']
          ce.ede('C:\\Users\\zhao\\Desktop\\xiugai.xls', i, 0, a)
          ce.ede('C:\\Users\\zhao\\Desktop\\xiugai.xls',i,1,b)
          ce.ede('C:\\Users\\zhao\\Desktop\\xiugai.xls', i, 2, c)
          ce.ede('C:\\Users\\zhao\\Desktop\\xiugai.xls', i, 3, o)
          ce.ede('C:\\Users\\zhao\\Desktop\\xiugai.xls', i, 4, p)
    except:
      print("订单查询结束")
test().down()