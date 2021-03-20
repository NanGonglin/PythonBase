# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/9 22:41
@Auth ： sy 
@Function ：请输入模块功能描述
"""
# # x，y是整数，z = |x| + |y|
# # 用编程实现，当x、y取不同值时，求z的值，打印出来
# # 需求分析：分情况：
# # 1.x,y都是非负数，z=x+y
# # 2.x是非负数，y是负数，z=x-y
# # 3.x是负数，y是非负数，z=-x+y
# # 3.x是负数，y是负数，z=-x-y
#
# # 定义一个函数
# def absSum(x,y):
#     if x > 0:
#         if y > 0:
#             z = x + y
#         else:
#             z = x - y
#     else:
#         if y > 0:
#             z = -x + y
#         else:
#             z = -x - y
#     return z
# print("请分别输入x,y的值，我来帮您计算z = |x| + |y|之后，z的值")
# 一次性输入四种情况测试
# for i in range(1,5):
#     x = input("请输入x的值：")
#     y = input("请输入y的值：")
#     x = int(x)
#     y = int(y)
#     z=absSum(x, y)
#     print("经过计算z = |x| + |y|，z的值是：", z)

# 求1-100内整数的和
# 题目分析：循环应该是1-100
#需求分析：使用in range(1,101)
# sum = 0
# for i in range(1, 101, 1):
#     sum += i
# print("1-100内整数的和是：", sum)


# 将课程九九乘法表，以while循环实现
#详见下面的九九乘法表代码

# 四舍五入保留两位小数
# x=input("输入一个数字，我可以四舍五入转换为两位小数形式:")
# x=float(x)
# x=round(x,2)
# print("四舍五入后的结果是：",x)

# 用户名和密码都是字符串，长度为6-16位，如何判断一个用户名和密码长度是否合法？
# 分析过程
# 1.判断用户名和字符串是否为空，如果都不为空，那么再判断长度是不是都在6-16，如果都符合6-16位，那么用户名和密码长度合法
# 2.用户名或者密码长度小于6或者大于16，不合法
# 3.用户名或者密码为空，不合法
def check(username,password):
    if username and password:
        if 5 < len(username) < 17 and 5 < len(password) < 17:
            print("结果：您输入的用户名和密码都是合法的")
        else:
            print("结果：您输入的用户名或密码长度不合法，正确的应该是6-16位")
    else:
        print("结果：您输入的用户名或密码为空，不合法")
for i in range(1,4) :
    print("请输入用户名和密码，我来帮您检测是否合法")
    username = input("用户名：")
    password = input("密码：")
    check(username,password)

# 九九乘法表只显示一半的三角形
#需求分析：只显示一半，就是只显示左下方的，右上方的不显示，那么就是只显示，列数小于等于行数的公式
#for写法
# for row in range(1,10,1):
#     for column in range(1,row+1,1):
#         print(row,"*",column,"=",row*column,end="\t")
#     print('\n')
#while写法：
# row=1
# while row <=9:
#     column=1
#     while column<=row:
#         print(row,"*",column,"=",row*column,end="\t")
#         column+=1
#     print("\n")
#     row+=1
# 九九乘法表去掉两条对角线
#需求分析，对角线的公式有两种情况：
#1.行数等于列数
#2.行数+列数的和等于10
#for写法
# for row in range(1,10,1):
#     for column in range(1,10,1):
#         if(row!=column and row+column!=10):
#             print(row,"*",column,"=",row*column,end="\t")
#         else:
#             print("         ",end="\t")
#     print('\n')

# #while写法：
# row=1
# while row <=9:
#     column=1
#     while column<=9:
#         if(row!=column and row+column!=10):
#             print(row,"*",column,"=",row*column,end="\t")
#         else:
#             print("         ", end="\t")
#         column+=1
#     print("\n")
#     row+=1