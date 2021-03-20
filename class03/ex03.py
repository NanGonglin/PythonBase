# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/10 14:14
@Auth ： sy 
@Function ：请输入模块功能描述
"""
# 元组
tup = ()
print(type(tup))
tup = (1,)
print(type(tup))
tup = (1, 2)
print(type(tup))

# 元组的增删改,不支持
# tup.append(2)
# del tup[1]

# 元组的查找
print(tup[1])
# 成员遍历
for t in tup:
    print(t)
# 下标遍历
for i in range(len(tup)):
    print(tup[i], end=',')

# 元组主要用于函数的返回，或者一些不让更改数据存储
list_tup = list(tup)
print(list_tup)
print(type(list_tup))
