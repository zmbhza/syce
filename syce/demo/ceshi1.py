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
# s = 0
# a = 1
# while  name():
#
#     s+=a
#     print (str(name()),s)
#     if name()=='左建国马建国左达王鑫':
#         break

print('小精灵：您好 ，欢迎来到古灵阁，请问您需要帮助吗，需要or不需要？')
a = input()
if a =='需要':
    b = input('请问您需要什么帮助？1.存款 2.货币兑换 3.咨询\n')
    if b =='1':
        print('小精灵：滚')
    elif b == '2':
        print('小精灵：金加隆和人民币的汇率为1:51.3，即一金加隆=51.3人民币')
        print('小精灵：请问您需要兑换多少金加隆呢')
        c = input()
        try:
            try:
                s = int(c)
                print('小精灵：好的，我知道了，您需要兑换'+str(s)+'金加隆')
                print('小精灵：那么您需要付给我'+str(s*51.3)+'人民币')
            except:
                s = float(c)
                print('小精灵：好的，我知道了，您需要兑换' + str(s) + '金加隆')
                print('小精灵：那么您需要付给我' + str(s * 51.3) + '人民币')
        except:
            print('滚')
    elif b == '3':
        print('小精灵：滚')
else:
    print('小精灵：滚')
