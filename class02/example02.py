# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/9 20:34
@Auth ： sy 
@Function ：请输入模块功能描述
"""
# 比较运算可以连写
x = 3
b = 1 < x < 4
print(b)

# 字符串的比较
# 比较大小时比较的是字符串中每一个字符对应得ascii的码
s1 = 'abcd'
s2 = 'abc'
print(s1 < s2)

# 相等和包含
print(s1 == s2)
print(s1.__contains__(s2))
