# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/16 20:18
@Auth ： sy 
@Function ：请输入模块功能描述
"""

# 导入库
# import time
# print(time.time())


# 导入包
# import class05
# 必须从项目的根目录导入包
# from class05 import p1


# 导入模块
# from class05 import ex01
# # import class05.ex01
#
# s = 'adefuadnerceadwguewadfowe'
# s = ex01.replace_sub(s, 4, 'ad', 'sr')
# print(s)
# ex01.test()


# 导入函数
from class05.ex01 import replace_sub

s = 'adefuadnerceadwguewadfowe'
s = replace_sub(s, 4, 'ad', 'sr')
print(s)
# 未导入的函数无法使用
# test()


# *的默认导入,就是默认导入class04的init.py文件中加入的类，需要在__init__.py提前写好
# from class04 import *
