# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/14 21:25
@Auth ： sy 
@Function ：请输入模块功能描述
"""

# 假设有一串数字是表示考试名次的，对这些名次进行排序,从小到大进行排序
rank=[3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]

# 用while语句实现冒泡排序
# 冒泡排序思想：
# 每一轮，将第n个数和第n+1个数进行比较，如果比较值与顺序不一致，就进行值交换,最多交换n-1-lun次,lun是已经排好序的数字
# 最多共进行n-1轮
# lun=0
# num=0
# while lun<len(rank)-1:
#     # len(height-lun-1)可以减少循环次数，因为每一轮比较厚，已经冒出来的元素是不用再比较的
#     #冒出来的元素已经全部放在了后面
#     while num<len(rank)-lun-1:
#         if rank[num+1]<rank[num]:
#             #如果第num+1个数的值小于第num个数的值，那么交换值
#             rank[num],rank[num+1]=rank[num+1],rank[num]
#         num+=1
#     lun+=1
#     #每一轮结束后，置num的值为0
#     num=0
# print(rank)

# 用while实现选择排序
# 选择排序思想：第n轮，以第1个数为最大数，记住下标，然后和后面的数做比较，找到最大值的下标，替换最大值和第一个数
# 第2轮，只需要比较前n-1个数，最多需要n-1轮
# lun=0
# while lun<len(rank)-1:
#     #每一轮比较，都会改变num的值，所以num的值需要重新赋值为0，每一轮比较，都可能改变max的值，所以max也重新赋值
#     max=0
#     num=0
#     while num<len(rank)-lun:
#         if rank[num]>rank[max]:
#             #如果当前下标元素的值比下标为max的元素的值大时，将max赋值为当前下标
#             max=num
#         num+=1
#         #交换最大值和最后一个未排序元素的值，将最大值放在最后
#     rank[len(rank)-lun-1],rank[max]=rank[max],rank[len(rank)-lun-1]
#     lun+=1
# print(rank)


# 用while实现杨辉三角
# 先将每行的系数打印，再打印空格格式
# 最多有n+1行
# 从第2行起，第n行的数，第一个和最后一个都是1，中间的数等于它肩膀上两数之和,最多有n+1个
#假设每个数占6个位置，最后一行，也就是第8行占了48个位置，最后一行就是6*yh
#所以第一行中间的位置就是3*yh
#后面每行空格就是3*(yh-row)
# yh = 8
# arr1 = [1]
# #先打印出第一行的空格，
# print('%*s' % (3 * yh, ''), end='')
# #打印第一行的数
# print('%6d' % arr1[0])
# arr2 = [1]
# #从第2行开始，即row=1
# row = 1
# while row < yh + 1:
#     column = 0
#     arr2.append(1)
#     while column < row:
#         if column == 0 or column == row - 1:
#             arr2[column] = 1
#         else:
#             arr2[column] = arr1[column - 1] + arr1[column]
#         column += 1
#     print('%*s' % (3 * (yh - row),''), end='')
#     for k in arr2:
#         print('%6d' % k, end='')
#     print()
#     row += 1
#     arr1 = arr2.copy()


# 字符串的替换，想替换第n个字符串
s='adefuadnerceadwguewadfowe'
s=s.replace('ad','sr',4)
s=s.replace('sr','ad',3)
print(s)







