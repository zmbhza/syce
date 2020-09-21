import random
import threading
def name():
    first_name = ["王", "李", "张", "刘", "赵", "蒋", "孟", "陈", "徐", "杨", "沈", "马", "高", "殷", "上官", "钟", "常",'左','右']
    second_name = ["伟", "华", "建国", "洋", "刚", "万里", "爱民", "牧", "陆", "路", "昕", "鑫", "兵", "硕", "志宏", "峰", "磊", "雷", "文","明浩", "光", "超", "军", "达"]
    name = random.choice(first_name) + random.choice(second_name)+random.choice(first_name)+random.choice(second_name)+random.choice(first_name) + random.choice(second_name)+random.choice(first_name) + random.choice(second_name)
    return name
def age():
    s = random.randint(18,99)
    return s
def sex():
    s = random.randint(0,1)
    return s
def address():
    first_name = ["王", "李", "张", "刘", "赵", "蒋", "孟", "陈", "徐", "杨", "沈", "马", "高", "殷", "上官", "钟", "常",'左']
    second_name = ["伟", "华", "建国", "洋", "刚", "万里", "爱民", "牧", "陆", "路", "昕", "鑫", "兵", "硕", "志宏", "峰", "磊", "雷", "文","明浩", "光", "超", "军", "达"]
    name = (random.choice(first_name) + random.choice(second_name)+random.choice(first_name)+random.choice(second_name)+random.choice(first_name) + random.choice(second_name)+random.choice(first_name) + random.choice(second_name))*2
    return name
s = 0
a = 1
while  name():

    s+=a
    print (str(name()),s)
    if name()=='左建国马建国左达王鑫':
        break
