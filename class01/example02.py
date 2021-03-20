# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/9 12:38
@Auth ： sy 
@Function ：请输入模块功能描述
"""

# 行，回车，分号不推荐
x = 1
y = 2

# 多行代表一个语句，用\反斜杠
s = '23dffvnfvjrtkkk.bmt' \
    'rmbtmbmntyn'
print(s)
print(s,
      'eferggrthrthwht')


# 不同层次的内容用缩进表示
def func1():
    print('这是函数,自己不会执行，需要被调用才会执行')


func1()

# 单行注释
"""
多行注释用多个双引号
"""
'''
这也是多行注释
'''

# 段落,是字符串的一种，可以直接换行
s = """这个
是一个
段落
字符串"""
print(type(s))
print(s)








