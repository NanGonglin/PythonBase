# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/20 13:19
@Auth ： sy 
@Function ：私有和公有函数
"""
class MyDog:
    """
    这个是__doc的内容
    """
    def __my_func(self):
        """私有函数，只能在类里面使用"""
        print("私有函数")
    def bark(self):
        self.__my_func()

if __name__=='__main__':
    dog=MyDog()
    dog.bark()

    #基础属性
    print(MyDog.__doc__)

    #基础函数
    dog.__getattribute__('bark')()











