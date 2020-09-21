class MusicPlayer(object):

    #记录第一个被创建对象的引用
    instance = None
    #记录是否执行过初始化动作
    init_flag = False

    def __new__(cls, *args, **kwargs):

        #1.判断类属性是否为空对象，若为空说明第一个对象还没被创建
        if cls.instance is None:
        #2.对第一个对象没有被创建，我们应该调用父类的方法，为第一个对象分配空间
            cls.instance = super().__new__(cls)
        #3.把类属性中保存的对象引用返回给python的解释器
        return cls.instance

    def __init__(self):

        #1.判断是否执行过初始化动作,若执行过，直觉return
        if MusicPlayer.init_flag:
            return

        #2.若没执行过，再执行初始化动作
        print("初始化init")

        #修改类属性的标记
        MusicPlayer.init_flag = True



#创建多个对象
player1 = MusicPlayer()
print(player1)

player2 = MusicPlayer()
print(player2)
