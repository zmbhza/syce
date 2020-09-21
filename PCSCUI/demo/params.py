from selenium.webdriver import ActionChains
import traceback,os,time
from twilio.rest import Client
#获取最新打开的浏览器，并且关闭上一个浏览器
def handles(a):
    a.close()
    n = a.window_handles
    a.switch_to.window(n[-1])
#断言，根据结果文案来判断
def act(a,b,c):
    try:
        assert a in b.find_element_by_xpath(c).text
        print('pass')
    except Exception as e:
        print("Assertion test fail", format(e))

#鼠标移动（仅移动，不触发任何操作）
def mouse_move(a,b):
    a.execute_script("arguments[0].scrollIntoView();",
    a.find_element_by_xpath(b))
    xpath = b
    move_on_to_add_condition = a.find_element_by_xpath(xpath)
    ActionChains(a).move_to_element(move_on_to_add_condition).perform()

# '''生成当前日期字符串'''
def currentDate():
    date = time.localtime()
    return '-'.join([str(date.tm_year), str(date.tm_mon), str(date.tm_mday)])

# '''生成当前时间字符串'''
def currentTime():
    date = time.localtime()
    return '-'.join([str(date.tm_hour), str(date.tm_min), str(date.tm_sec)])

# '''创建当前日期和当前时间目录'''
def createDir():
    path = os.path.dirname(os.path.abspath(__file__))
    dateDir = os.path.join(path, currentDate())
    # 如果当前日期目录不存的话就创建
    if not os.path.exists(dateDir):
        os.mkdir(dateDir)
    timeDir = os.path.join(dateDir, currentTime())
    # 如果当前时间目录不存的话就创建
    if not os.path.exists(timeDir):
        os.mkdir(timeDir)
    return timeDir

#屏幕截图
def takeScreenshot(driver,savePath,pictureName):
    time.sleep(2)
    picturePath = os.path.join(savePath, pictureName+'.png')
    try:
        driver.get_screenshot_as_file(picturePath)
    except Exception  as e:
        print(traceback.print_exc(e))

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