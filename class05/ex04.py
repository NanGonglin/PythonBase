# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/17 19:56
@Auth ： sy 
@Function ：请输入模块功能描述
"""
#函数的传值与传地址

#传值
def my_func(a,b):
    """
    形参，局部变量，只在这个函数里面有效
    :param A: 形参
    :param B: 形参
    :return:
    """
    a=3
    print(a)
#传值，实参，在这个文件里面有效
A=B=2
my_func(A,B)
print(A,B)



#传地址
def my_func_all(list1):
    list1[1]=5
    #一定不能改变容器变量本身，只能改变容器内部的东西
    # list1=[3]
    print(list1)

list2=[1,2,4]
my_func_all(list2)
print(list2)


#浅复制和深复制
#浅复制，只复制了容器，未复制容器的值，如果源容器的值变化，会跟着一起变化,类似于地址传递
l1=[1,2,3]
l2=l1
l2[1]=22
print(l1)
#深复制,全部复制到了另外一个地方，源容器与新的容器没有关系
# l3=l2.copy()
#截取产生一个新的列表,和深复制一样
l3=l2[:]
l3[2]=33
print(l2)


#函数的返回
def my_func3():
    # 返回可以是一个变量，
    # 可以是一个元组
    return 1,2,3

res=my_func3()
print(res)



