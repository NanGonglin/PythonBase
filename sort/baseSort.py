# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/18 14:41
@Auth ： sy 
@Function ：请输入模块功能描述
"""
from class06.decorator import dec_time


# 将选择、冒泡、快排整理成一个模块，放在一个包里面，做成自己的库
# 尝试比较一下，三个排序算法的效率
# 冒泡排序思想：
# 每一轮，将第n个数和第n+1个数进行比较，如果比较值与顺序不一致，就进行值交换,最多交换n-1-lun次,lun是已经排好序的数字
# 最多共进行n-1轮
@dec_time('ms')
def bubble_sort(rank):
    lun = 0
    num = 0
    while lun < len(rank) - 1:
        # len(height-lun-1)可以减少循环次数，因为每一轮比较厚，已经冒出来的元素是不用再比较的
        # 冒出来的元素已经全部放在了后面
        while num < len(rank) - lun - 1:
            if rank[num + 1] < rank[num]:
                # 如果第num+1个数的值小于第num个数的值，那么交换值
                rank[num], rank[num + 1] = rank[num + 1], rank[num]
            num += 1
        lun += 1
        # 每一轮结束后，置num的值为0
        num = 0
    return rank


# 选择排序思想：第n轮，以第1个数为最大数，记住下标，然后和后面的数做比较，找到最大值的下标，替换最大值和第一个数
# 第2轮，只需要比较前n-1个数，最多需要n-1轮
@dec_time('ms')
def select_sort(rank):
    lun = 0
    while lun < len(rank) - 1:
        # 每一轮比较，都会改变num的值，所以num的值需要重新赋值为0，每一轮比较，都可能改变max的值，所以max也重新赋值
        max = 0
        num = 0
        while num < len(rank) - lun:
            if rank[num] > rank[max]:
                # 如果当前下标元素的值比下标为max的元素的值大时，将max赋值为当前下标
                max = num
            num += 1
            # 交换最大值和最后一个未排序元素的值，将最大值放在最后
        rank[len(rank) - lun - 1], rank[max] = rank[max], rank[len(rank) - lun - 1]
        lun += 1
    return rank


# 快速排序
@dec_time('ms')
def quick_sort(rank, left, right):
    """
    快速排序思想：
    先找一个基准值，比如找最左边的第一个为基准值，开始从右往左变了，如果有比基准值小的，那么就和基准值交换位置，
    交换完位置后，再从左向右遍历，如果有比基准值大的，那么和基准值交换位置，直到基准值左边的数都比基准值小，右边的数都比基准值大
    如果在遍历过程中左边的数都比基准值小，右边的数都比基准值大，那么基准值右移一位，进行递归循环。
    递归循环时，基准值分别是左边的第一个数和右边的第一个数。递归的出口是左边只剩一个数，右边只剩一个数
    :param rank: 待排序的列表
    :param left: 未排序的列表左边第一个元素
    :param right: 未排序的列表右边第一个元素
    :return:
    """
    # 基准值为左边第一个
    base = rank[left]
    l = left
    h = right
    # 所有值遍历完
    while l < h:
        # 从右向左遍历
        while l < h:
            # 如果右边有比基准值小的，交换位置
            if rank[h] < base:
                rank[h], rank[l] = rank[l], rank[h]
                # 左边右移
                l += 1
                break
            else:
                # 没有比基准值小的，
                h = h - 1

        # 从左向右遍历
        while l < h:
            # 如果有比基准值大的，交换位置
            if rank[l] > base:
                rank[l], rank[h] = rank[h], rank[l]
                # 右边左移
                h = h - 1
                break
            else:
                l += 1
    # 左边排序完成
    if l <= left:
        pass
    # 如果左边排序未完成，就递归
    else:
        quick_sort(rank, left, l - 1)
    # 右边排序完成
    if h >= right:
        pass
    # 右边排序未完成，递归
    else:
        quick_sort(rank, h + 1, right)


# 导入时间的类
# import time

# def compare_time(rank,method):
#     """
#     比较三个算法的函数
#     :param rank: 随机生成的数组
#     :param method: 使用的排序算法
#     :return:
#     """
#     start = time.time()
#     if method=='bubble_sort':
#         bubble_sort(rank)
#         end=time.time()
#         print('1000个随机数使用冒泡排序所用时间是',end-start)
#     elif method=='select_sort':
#         select_sort(rank)
#         end = time.time()
#         print('1000个随机数使用选择排序所用时间是', end - start)
#     elif method=='quick_sort':
#         quick_sort(rank,0,len(rank)-1)
#         end = time.time()
#         print('1000个随机数使用快速排序所用时间是', end - start)

# python的默认最大递归次数为1000左右，通过导入系统的类，使得最大递归次数大于1000次
import sys

sys.setrecursionlimit(1000000)

# 假设有一串数字是表示考试名次的，对这些名次进行排序,从小到大进行排序
# rank=[3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
import random

rank = random.sample(range(0, 1001), 1000)
bubble_rank = rank
# # compare_time(bubble_rank,'bubble_sort')
select_rank = rank
# # compare_time(select_rank,'select_sort')
quick_rank = rank
# # compare_time(quick_rank,'quick_sort')


bubble_sort(bubble_rank)
select_sort(select_rank)
# quick_sort(quick_rank,0,len(quick_rank)-1)
