# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/20 13:19
@Auth ： sy 
@Function ：请输入模块功能描述
"""
from class06.ex01 import Dog
from class06.ex02 import s as sss

print(sss)


class Black_Dog:
    def __init__(self):
        self.color = '黑色'

    def catch_mouse(self):
        print('黑狗抓耗子')

    def my_color(self):
        print(self.color)


# 不建议使用多继承
# class China_Dog(Dog,Black_Dog):
class China_Dog(Dog):
    """派生类，继承基类，中华狗继承Dog类"""

    def __init__(self, w, c, n):
        """
        如果子类显示定义了构造函数，那么必须要在子类的构造函数中使用下面两种方法，去调用父类的构造函数
        """
        """重写父类的构造方法"""
        super().__init__(w, c, n)
        Dog.__init__(self, w, c, n)

    def run(self):
        """父类不满足子类的需求的时候，子类可以重写父类的方法"""
        print('重写后的方法')

    def my_dog_play(self):
        """扩展"""
        print("狗子喜欢玩皮球")


if __name__ == '__main__':
    # 继承了类方法和类属性
    print(China_Dog.dog_type)

    dog = China_Dog(3, '白色', '小白')
    print(dog.name)
    dog.catch_mouse()
    dog.run()
    dog.my_dog_play()
