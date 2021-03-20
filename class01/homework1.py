# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/14 21:26
@Auth ： sy 
@Function ：请输入模块功能描述
"""
# 面向过程的示例，起床，穿衣，刷牙，洗脸，上课
print('起床')
print('穿衣')
print('刷牙')
print('洗脸')
print('上课')



# 设x=3,y=4,z满足x的平方+y的三次方，打印z的值
x = 3
y = 4
z = x ** 2 + y ** 3
print('z的值是',z)


# 你老婆对你说：“老公，晚上回来买一个西瓜，如果看到西红柿，就买两个。”
# 请用程序打印你从下班，到家的全过程
"""
def func1(thing):
    if thing == '西红柿':
        print('买了', thing, thing, '西瓜')
    else:
        print('买了', '西瓜')
print('假设回家路上看到了西红柿，那么')
func1('西红柿')
print('假设回家路上没有看到西红柿')
func1('苹果')
"""


s=input("请输入：")
print(s)
print(type(s))