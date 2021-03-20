# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/20 13:19
@Auth ： sy 
@Function ：请输入模块功能描述
"""
# 全局变量
s = ''


def ttt():
    #代表s是引用的全局变量
    global s
    # 局部变量
    x = 3
    y = 0
    z = 0
    if x > 1:
        # 变量定义在子过程中，只在子过程中生效，成为局部变量
        y = 2
        s = 'abc'
    else:
        z = 3
    print(y, z)


ttt()
print(s)
