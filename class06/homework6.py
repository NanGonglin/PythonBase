# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/20 21:55
@Auth ： sy 
@Function ：请输入模块功能描述
"""
#人类，男人类，女人类,体现类的继承
class human:
    #类变量
    human_type='高级动物'
    human_kind='人都有手有脚'
    """父类，人类"""
    def eat(self):
        print('人类一日三餐')

    """类方法"""
    @classmethod
    def sport(self):
        print('人类喜欢运动')

    def __init__(self,name):
        """构造函数，用于在创建对象的时候创建实例变量"""
        self.name='人类'

class man(human):
    # 类变量
    man_type='雄性动物'
    """子类，男人类，继承父类人类"""
    def play(self):
        """子类扩展的方法"""
        print('男人喜欢玩冒险的')

    """类方法"""
    @classmethod
    def man_sport(cls):
        print('男人喜欢练肌肉')

    def __init__(self,name):
        """构造函数，用于在创建对象的时候创建实例变量"""
        self.name='男人'

class woman(human):
    # 类变量
    woman_type = '雌性动物'
    """子类，女人类，继承父类人类"""
    def eat(self):
        """重写父类的eat方法"""
        print('女人喜欢吃麻辣烫')

    """类方法"""
    @classmethod
    def woman_sport(cls):
        print('女人喜欢瘦成一道闪电')

    def __init__(self,name):
        """构造函数，用于在创建对象的时候创建实例变量"""
        self.name='女人'

if __name__=='__main__':
    people=man('李明')
    #继承父类的eat
    people.eat()
    #子类扩展自己的方法
    people.play()

    lady=woman('韩梅梅')
    #使用重写的方法
    lady.eat()

    #直接使用自己的类方法
    human.sport()
    man.man_sport()
    woman.woman_sport()

    #使用类变量
    print(human.human_type)
    print(man.man_type)
    print(woman.woman_type)

    human=human('人类老大')
    # 调用实例变量
    print(human.name)
    print(people.name)
    print(lady.name)

    #属性的继承
    print(people.human_kind)
    print(lady.human_kind)





