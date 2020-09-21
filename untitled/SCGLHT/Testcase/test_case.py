import requests
from params import params as p
import pytest
import json
import allure
import os
from test_aasd import test_demo as demo
a = str(p.num())
s = (p.payload())

class Test_SPGL():
    """测试模块"""
    def setup_class(self):
        """商品管理后台登录"""
        name = p.get_value('login')
        url= name['url']
        payload = name['payload']
        headers = name['headers']
        re = requests.request("POST", url, data=json.dumps(payload), headers=headers)
        global access_token
        access_token = re.json()["body"]["access_token"]
        p.msg(re,'查')
        print('开始执行用例')

    def test_SPPP_02(self):
        """商品管理-商品管理-查询"""
        name = p.get_value('SPGL_CX')
        url = name ['url']
        payload = name['payload']
        global headers
        headers = p.headers(access_token)
        re = requests.request("POST", url, data=json.dumps(payload), headers=headers)
        p.msg(re, '查')

    def test_SPPP_211(self):
        """商品管理-商品品牌-新增"""
        p.T(0.5)
        name = p.get_value('SPPP_XZ')
        url = name['url']
        payload = {"name":"测试"+a,"logoUrl":"https://productimage.zhaolaobao.com/d6b292b4_942b_b5c1_69dc_1d2ca913d17b","hot":"","fileType":"image/jpeg"}
        #headers ={'Authorization':"Bearer "+str(access_token),'Content-Type': 'application/json','Cookie': 'JSESSIONID=0FC830428EC9F729E13984459E3DF8E6; shareSessionId=0FC830428EC9F729E13984459E3DF8E6'}
        re = requests.request("POST", url, data=json.dumps(payload), headers=headers)
        p.msg(re,'查')
    def test_SPPP_222(self):
        """商品管理-商品品牌-查询"""
        p.T(0.5)
        name = p.get_value('SPPP_CX')
        url = name['url']
        payload = {"likeName":a,"sort":'',"page":1,"pageSize":10,"scouce":1}
        re = requests.request("POST", url, headers=headers, data=json.dumps(payload))
        p.msg(re,'查')
        global bb
        bb = re.json()['body']['list'][0]['id']

    def test_SPPP_334(self):
        """商品管理-商品品牌-删除"""
        p.T(0.5)
        name = p.get_value('SPPP_SC')
        url = name['url']
        payload = {"id":bb}
        re = requests.request("POST", url, headers=headers, data = json.dumps(payload))
        p.msg(re,'删')
    def teardown_class(self):
        print('所有用例执行完毕')

if __name__ == '__main__':
    pytest.main(['-s','-q',r'C:\Users\zhao\PycharmProjects\untitled\SCGLHT\Testcase\test_case.py','--alluredir','./report','--clean-alluredir'])
    os.system('allure generate report/ -o report/html --clean')

