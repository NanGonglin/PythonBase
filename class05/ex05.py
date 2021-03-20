# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/17 22:41
@Auth ： sy 
@Function ：请输入模块功能描述
"""
#递归
#递归必须要有一个出口

def factor(n):
    """
    #求n的阶乘,类似于堆栈的形式，先进后出
    :param n: n*(n-1)!
    :return:
    """
    if n>1:
        return n*factor(n-1)
    else:
        return 1

res=factor(5)
print(res)












