# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/9 20:21
@Auth ： sy 
@Function ：请输入模块功能描述
"""

# 浮点型运算,存储的都是双精度
# （根号3）的平方
x = (3 ** 0.5) ** 2
y = 3 ** 0.5 ** 2
print(x)
print(y)
# 四舍五入
x = round(x, 2)
print(x)

# 优先级
y = 4 - 5 * 3 / 2 ** 3
print(y)

# 字符串算数运算
# 相加，相乘
s1 = 'abc'
s2 = 'cde'
# 拼接
print(s1 + s2)
print(s1 + str(1))
# 重复多少次
print(s1 * 3)

x=1
y=2
z=3
print(x<y and x<z)