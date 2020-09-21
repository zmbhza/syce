import random
import yaml,os
import warnings
warnings.filterwarnings("ignore")

def keyboard(a,i):
    #控制数字键盘输入以及长度
    b = 0
    for s in range(10) :
        q = random.randint(0, 9)
        s+=b
        a.hidden_wait = 20.0 #隐式等待
        a(resourceId="com.tencent.mm:id/tenpay_keyboard_"+str(q)).click()
        if i == s :
            break
###yaml文件

def get_value(key_name):
    """
    获取yaml文件
    :param value:
    :return:
    """
    path_dir = str(
        os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
    yamlPath = path_dir + '\\Resources\\xpath.yaml'
    f = open(yamlPath, 'r', encoding='utf-8')
    y = yaml.load_all(f)
    try:
        for data in y:
            if data['name'] == key_name:
                return data
    except Exception:
        raise
    a = get_value('aaa')
    print(a['url'])