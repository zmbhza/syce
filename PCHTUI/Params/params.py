import os
import yaml
import random
import time
import string
import pymysql
from twilio.rest import Client
from pywinauto import Desktop   #导入Desktop库，实现对windows系统桌面进行操作
from pywinauto.keyboard import send_keys   #导入send_keys库，实现模拟键盘操作
from Params.index import Comm,mysql,sql
from email.mime.text import MIMEText
import smtplib
###定义随机数，预防重复
global r
r = Comm()
def num():
    a = random.randint(0,10000)+random.randint(0,10000)
    s = a
    return s
###随机生成N位数字，做手机号拼接使用
def rdm(a):
    seeds = string.digits
    random_str = random.sample(seeds, k=a)
    s = ("".join(random_str))
    return s
###等待时间
def T(a):
    time.sleep(a)

###yaml文件
path_dir = str(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
def get_value(key_name):
    """
    获取yaml文件
    :param value:
    :return:
    """
    yamlPath = path_dir + '\\Params\\file.yaml'
    f = open(yamlPath, 'r', encoding='utf-8')
    y = yaml.load_all(f)
    try:
        for data in y:
            if data['name'] == key_name:
                return data
    except Exception:
        raise
#从windows中上传图片
def win_click(a,b):
    app = Desktop()  #创建操作桌面的对象
    time.sleep(0.5)
    dlg = app["打开"]   #获取弹窗的窗口标题
    #dlg.print_ctrl_ids()   打印窗口的所有控件信息
    time.sleep(0.5)
    dlg["地址: xiaominToolbar"].click()   #获取文件路径填写输入框并点击
    time.sleep(0.5)
    send_keys(a)     #在文件路径填写输入框输入文件存在的路径
    send_keys("{VK_RETURN}")  #输入文件路径后按回车键
    time.sleep(0.5)
    dlg["文件名(&N):Edit"].type_keys(b)  #获取文件名输入框并填写文件名
    time.sleep(0.5)
    #send_keys("{VK_RETURN}")
    dlg["打开(&O)"].click()  #获取“打开”控件并点击
    time.sleep(1.5)

#foucs聚焦到页面某一点位
def focus(a):
    target = r.driver.find_element_by_xpath(a)
    r.driver.execute_script("arguments[0].scrollIntoView();", target)

#根据下拉列表来选择对应的控件
def list(a,b,c):
    r.click('xpath',a)
    time.sleep(0.3)
    department = r.driver.find_elements_by_xpath(b)
    for li in department:
        if c in li.text:
            li.click()
            break

#数据库查询新增或删除数据
# 1、连接MySQL数据库
def sql_select(aa,bb,cc,dd):
    s = mysql(cc)
    c = s.cursor()
    sq = sql(dd)   # 2、读user表的数据
    c.execute(sq,aa)   # 执行sql语句
    try:
        ((row,),) = c.fetchall()    # 全部读出来
        print(row)
        if bb in row:
            print('查询到新增数据')
        else:
            print('未查询到对应的数据') #删除库中信息后可报此错误
    except:
        print('代码异常')
    c.close() #关闭数据库链接

#发送短信
def send_msg(message):
    account_sid = 'AC7b56757e55dad8a593ab9350e7b7075f'
    auth_token = 'fd7c198c5e22d44558e73593945cf223'
    # 实例化
    client = Client(account_sid, auth_token)
    u'自定义短信内容message'
    msg = client.messages.create(
        to='+8617611520838',  # 要给谁发短信, 必须带区号, 中国要加上+86
        from_='+19548002273',  # 你自己twilio网站申请的手机号码, 必须带上+号
        body=message  # 你的短信内容
    )

#发送邮件
def email(a,b):
    msg = MIMEText(a)
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
email('a','b')