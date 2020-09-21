import json

def name(a):
    if a =='登录':
        s = 'http://admin.bsapo.com/api/uc/userFront/login/nologin'
        return s
    elif a == '首页刷新':
        s = ''
        return s
    elif a == '删除'  :
        s = ''
        return s
def payload(a):
    if a =='登录':
        s = {
    "username":"17611520838",
    "password":"iFnSP6CafCLdrV/9mjlSnA==",
    "automatic":"0",
    "source":"1",
    "code":"",
    "randString":"oLOFnn3cqxmrhXtX",
    "wechatCode":""
    }
        return s
    elif a == '商品管理':
            s = ''
            return s
    elif a == '':
        ''
    elif a == '':
        ''
def headers(a):
    if a =='非登录':
        b = {
            'cache-control': "no-cache",
            'Postman-Token': "0dc23c64-e110-4753-8b84-313acff1c11c"
        }
        return b