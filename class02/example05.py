# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/9 21:26
@Auth ： sy
@Function ：请输入模块功能描述
"""
# 每周1-5都要上班，6-7玩
# 怎么把每周的每一天要做的事情都打出来?
# day = input("今天是星期几，请输入：")
# day = int(day)
# if day < 1 or day > 7:
#     print('输入错误，程序结束')
#     exit(0)
# while day <= 7:
#     if day < 6:
#         print("星期" + str(day) + "上班")
#         day+=1
#     else:
#         print("星期" + str(day) + "玩")
#         day+=1
    # 必须注意改变循环控制条件
    # 打印完一天后进入下一天
    # day += 1
    # # 跳出当前循环，不管条件达到与否
    # break


#for 循环,成员遍历
#按存储
# for s in [1,2,3,4,5]:
#     print(s,end=',')

#求1-100以内整数的和
#循环99次
#开始，结束，步长
#[开始，结束)，左闭右开，
# for i in range(1,101,1):
#     print(i,end=",")

#打印九九乘法表
#0<x<10,x<y<10的整数，求x*y
x=1
while x <=9:
    y=1
    while y<=9:
        print(x, "*", y, "=", x * y, end="\t")
        y += 1
    print("\n")
    x += 1











