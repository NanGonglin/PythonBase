# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/13 13:40
@Auth ： sy 
@Function ：请输入模块功能描述
"""
#列表用while遍历实现
#需求分析：定义一个变量，从0开始遍历,一直到len(list)
# list=[23,34,45,2,31,False,43,56,67,' ',1]
# i=0
# while i<len(list):
#     print(list[i],end=',')
#     i+=1

#元组用while遍历实现
# tup=('False',23,55,67,8,87,95,5,'')
# i=0
# while i<len(tup):
#     print(tup[i],end=',')
#     i+=1


#字典四种遍历实现
#需求分析：字典的四种遍历分别是，键遍历，值遍历，字典项遍历，键值对遍历
# teacher={'will':'python老师','roy':'java老师','tufei':'性能测试老师','kaka':'课程顾问'}
# print('\n'+'字典的键遍历：')
# for key in teacher.keys():
#     print(key)
#
# print('\n'+'字典的值遍历：')
# for value in teacher.values():
#     print(value)
#
# print('\n'+'字典每一项遍历：')
# for kv in teacher.items():
#     print(kv)
#
# print('\n'+'字典的键值对遍历：')
# for key,value in teacher.items():
#     print(key,value)

#自己去抓包，把ip接口的返回结果处理为标准json字符串；再使用json库，把字符串转为dict，并打印你所在地区的location
import json
ipResult={"country":"中国","province":"北京","city":"北京","county":"丰台","isp":"航数宽带"}
#转json字符串时，如果乱码，可以在转的时候加上ensure_ascii = False，解决乱码问题
json_ipResult=json.dumps(ipResult,ensure_ascii = False)
print('标准字符串的结果是:',json_ipResult)
#将json字符串转为字典的键值对形式
dict_ipResult=json.loads(json_ipResult)
print('字典结果是:',dict_ipResult)
#打印所在地区的location,只打印中国，城市北京，县，和航数宽带，不打印省
#定义字符串的初始值为空值
str=''
for key,value in dict_ipResult.items():
    if key!='province' and key!='isp':
        str+=value+' '
    elif key!='province':
        str+='\n'+value
print(str)


