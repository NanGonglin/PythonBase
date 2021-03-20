# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/9 21:26
@Auth ： sy 
@Function ：请输入模块功能描述
"""
# 输入x，y是整数，z = |x| + |y|
"""
需求分析：
有几种情况：
1.输入的不是整数（异常处理，暂不讲）
2.x,y都是非负数
3.x是正数，y是负数
4.x是负数，y是正数
5.x是负数，y是负数
"""
# x = input("请输入x:")
# y = input("请输入y:")
# x = int(x)
# y = int(y)
# 第一种写法
# if x >= 0 and y >= 0:
#     z = x + y
# elif x >= 0 and y < 0:
#     z = x - y
# elif x < 0 and y >= 0:
#     z = -x + y
# else:
#     z = -x - y
# print(z)

# 第二种写法
if x >= 0:
    if y >= 0:
        z = x + y
    else:
        z = x - y
else:
    if y >= 0:
        z = -x + y
    else:
        z = -x - y
print(z)

# 如果只需要处理条件成立的情况，而不成立的情况不需要做任何事
# 输入x是正数，求z=|x|
x = input("请输入x:")
x = int(x)
z = x
if x < 0:
    z = -x
print(z)
