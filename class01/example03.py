# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/9 12:56
@Auth ： sy 
@Function ：四大数据类型
"""

# 整型：int
x = 1
print(x)
print(type(x))

# 小数：float，双精度
y = 1.2
print(y)
print(type(y))

# 布尔 bool
b = True
c = False
print(b)
print(type(c))
print(int(c))

# 字符串 str
s = 'deferfrewfwerfref'
print(type(s))
print(s)

# 转义 \
# 特殊字符转普通字符含义
s = 'deefef\'ce\\ffer'
print(s)
# 普通字符转特殊含义
s = 'eceferf\n\tefwe'
print(s)

# 互斥,前三种统称为数字类型，字符串是字符串
# 互斥：数字类型和字符串是不能在运算里面共同操作
print(x)
print(y)
print(b)
print(x + y + b)
# print(x+s) 报错，类型不同

# 互转
x = 1
s = 1.11
# int(小数) 对小数取整
print(x + int(s))
#整数可以转化为小数
print(float(x))

#字符和其他类型的转化
#原则必须符合语法规则
s = '1.11'
x = 2
print(x)
print(x + float(s))
#数字转为字符串
print(s+str(x))

#bool值的转换
#0，'',None都是转为False
s='False'
print(bool(s))
s=''
print(bool(s))
#print(int(s))
