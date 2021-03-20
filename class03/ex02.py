# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/10 14:14
@Auth ： sy 
@Function ：请输入模块功能描述
"""
# 列表
name = []
print(id(name))
name = ['will', 'roy', '土匪']
print(name)
# 每一个值都相当于一个变量
name = ['will', 'roy', '土匪', 1, True, 1.1]
print(name)

# 列表的增加
# append在列表的末尾添加
name.append('sy')
print(name)
# insert在指定位置添加元素
# 下标，从0开始，到列表长度减1
name.insert(1, 'kk')
print(name)

# 列表的删除
# remove在删除的时候，如果有多个一样的元素，那么只会删除找到的第一个元素;如果没有，就会报错
name.remove('kk')
print(name)
# del按下标删除元素
del name[1]
print(name)
# 删除下标的元素
name.pop(1)
print(name)
# clear清空元素
# name.clear()
# print(name)

# 列表的更新
name[1] = '大土匪'
print(name)
# copy元素的复制
name1 = name.copy()
print(name1)
print(id(name1))

# 列表的拼接
name2 = ['x', 'y', 'z']
name2 = name2 + name
print(name2)

# 列表的截取,左闭右开的原则
print('列表的截取',name2[1:5])
print(name2[:4])
print(name2[4:])
print(name2[:])

# 列表的反转
print(name2[::-1])
print(name2[::1])
# 列表截取，有三个参数，s开始位置,e结束位置,step步长
print(name2[len(name2)::-1])
print(name2[:len(name2):1])

# 列表的查找：取值
print(name2[1])
print(name2.__getitem__(1))

# 列表的遍历
# 下标遍历
height = [23, 56, 12, 76, 87, 45, 98]
for i in range(len(height)):
    height[i] += 1
print(height)
#成员遍历,只能读取元素，不能操作元素
for h in height:
    h=h+1
    print(h)
print(height)
print(type(height))