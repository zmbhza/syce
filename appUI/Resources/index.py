def click(a,b,c):
    #点击事件
    if a =='text':
        b.hidden_wait = 20.0  # 隐式等待
        b(text=c).click()
    elif a =='xpath':
        b.hidden_wait = 20.0  # 隐式等待
        b.xpath(c).click()
def input(b,c,d):
    #普通输入框输入
    b.hidden_wait = 20.0  # 隐式等待
    b(text=c).set_text(d)