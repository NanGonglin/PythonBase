# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/13 14:03
@Auth ： sy 
@Function ：请输入模块功能描述
"""
# 字符串的处理

# 字符串的切割，可以按字符分割，也可以按字符串分割
import json

# str = "ie=utf-8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=ip&fenlei=256&t"
# s = str.split('&')
# print(s)
# print(type(s))
# params = {}
# for key_value in s:
#     index = key_value.find('=')
#     if index > 0:
#         key = key_value[:key_value.find('=')]
#         value = key_value[key_value.find('=') + 1:]
#     else:
#         key = key_value
#         value = None
#     params[key] = value
# print(params)
# print(json.dumps(params))

# 字符串的反转和截取：可以把字符串看成一个字符列表，和列表就一样了
s = '123'
s = s[::-1]
print(s)

# 字符串的替换
s = 'will,roy,tufei,kaka,tufei,roy,will'
# replace(old,new,num) old是需要替换的字符 new:替换的字符，count替换次数，默认是全部，也就是-1
s = s.replace('will', 'youmi', 3)
print(s)
# 替换最后一个字符
s = s[::-1]
s = s.replace('imuoy', 'lliw', 1)
s = s[::-1]
print(s)

# 课外作业：只想替换第n个，怎么办，有就替换，没有就不替换

