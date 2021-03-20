# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/20 13:19
@Auth ： sy 
@Function ：请输入模块功能描述
"""

#类的定义，类名符合变量的命名规则，一般首字母大写
class Dog:
    """定义一个狗类"""
    #类变量
    dog_type='狗'

    def __init__(self,weight,color,name):
        """构造函数，用于创建对象，并且在创建对象的时候创建实例变量，self表示实例本身"""
        self.weight=weight
        self.color=color
        self.name=name

    def catch_mouse(self):
        """实例函数，必须使用对象来调用"""
        print("狗拿耗子")

    def run(self,*args):
        print("小狗跑起来了")
    #类的方法，cls表示类本身，使用的时候不需要传
    @classmethod
    def bark(cls):
        """类方法，狗叫"""
        print('狗叫：汪汪汪')

    def  __my_func(self):
        """私有方法不会被继承"""
        print("私有方法不会被继承")



if __name__=='__main__':
    #类属性和类方法，不需要创建变量，可以直接使用
    #类属性
    print(Dog.dog_type)
    #类方法
    Dog.bark()

    dog=Dog('5',"白色",'小白')
    print(dog.name)

    dog1 = Dog('4', "黑色", '小黑')
    print(dog1.name)

    #对于实例函数和变量，必须要创建对象，通过对象去调用，因为他们是属于特定对象的
    # dog=Dog()
    # print(dog.name)
    # print(dog.catch_mouse())

    #不建议修改类变量，一旦修改，所有引用的都会发生改变
    # Dog.dog_type='人'
    # print(dog.dog_type)

























