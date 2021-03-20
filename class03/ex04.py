# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/13 12:57
@Auth ： sy 
@Function ：请输入模块功能描述
"""
# 字典,主要用于接口测试
stu = {}
print(stu)
print(type(stu))
# 一般通常键的类型都是字符串，值的类型是任意的
a=3
stu = {'key1': 'value1', 1: 2, False: 3,2:a}
print(stu)


#字典的元素增加,新增不存在的键就相当于增加，新增已存在的键就等于修改
stu['tufei']=172
print(stu)
#字典元素的修改
stu['tufei']=175
print(stu)

#字典的删除
stu.pop(False)
print(stu)
del stu[1]
print(stu)

#通过键获取对应值
print(stu.get('tufei'))
#当键不存在的时候，下面会报错，上面通过get的结果是空
print(stu['tufei'])

#字典元素的更新,键已存在就是更新，不存在就是新增键值对
stu.update({'tufei':177,'key1':180,'will':172})
print(stu)

#字典与json互转
import json
#字典转json字符串
json_stu=json.dumps(stu)
print(json_stu)
#json字符串转字典
stu1=json.loads(json_stu)
print(stu1)


#键的遍历
for key in stu1:
    stu1[key]=str(stu1[key])+'1'
    print(stu1.get(key))

print(list(stu1.keys()))
for key in stu1.keys():
    print(key)

#值的遍历
print(list(stu1.values()))
for key in stu1.values():
    print(key)


#键值对的遍历
for key,value in stu.items():
    print(key,value)



