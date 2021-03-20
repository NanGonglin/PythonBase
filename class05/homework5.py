# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/18 12:15
@Auth ： sy 
@Function ：请输入模块功能描述
"""


# 快速排序
# def quick_sort(rank,left,right):
#     """
#     快速排序思想：
#     先找一个基准值，比如找最左边的第一个为基准值，开始从右往左变了，如果有比基准值小的，那么就和基准值交换位置，
#     交换完位置后，再从左向右遍历，如果有比基准值大的，那么和基准值交换位置，直到基准值左边的数都比基准值小，右边的数都比基准值大
#     如果在遍历过程中左边的数都比基准值小，右边的数都比基准值大，那么基准值右移一位，进行递归循环。
#     递归循环时，基准值分别是左边的第一个数和右边的第一个数。递归的出口是左边只剩一个数，右边只剩一个数
#     :param rank: 待排序的列表
#     :param left: 未排序的列表左边第一个元素
#     :param right: 未排序的列表右边第一个元素
#     :return:
#     """
#     #基准值为左边第一个
#     base=rank[left]
#     l=left
#     h=right
#     #所有值遍历完
#     while l<h:
#         #从右向左遍历
#         while l< h:
#             #如果右边有比基准值小的，交换位置
#             if rank[h]<base:
#                 rank[h],rank[l]=rank[l],rank[h]
#                 #左边右移
#                 l+=1
#                 break
#             else:
#                 #没有比基准值小的，
#                 h=h-1
#
#         #从左向右遍历
#         while l<h:
#             #如果有比基准值大的，交换位置
#             if rank[l]>base:
#                rank[l],rank[h]=rank[h],rank[l]
#                #右边左移
#                h=h-1
#                break
#             else:
#                 l+=1
#     #左边排序完成
#     if l<=left:
#         pass
#     #如果左边排序未完成，就递归
#     else:
#         quick_sort(rank,left,l-1)
#     #右边排序完成
#     if h>=right:
#         pass
#     #右边排序未完成，递归
#     else:
#         quick_sort(rank,h+1,right)
#
# rank=[3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
# quick_sort(rank,0,len(rank)-1)
# print(rank)

# 用循环实现快速排序
# 循环递归思想：同样选取左边第一个为基准值，先从右向左排序，如果有比基准值小的，那么和基准值交换位置
# 然后从左向右排序，左边有比基准值大的，那么和基准值交换位置，反之不交换位置也不改变方向。
# 循环条件是，左边只剩一个数，右边剩一个数
# rank=[3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
# left=0
# right=len(rank)-1
# l=left
# h=right
# base=rank[left]
# # while l<h:
# while l<h:
#     while l<h:
#         if rank[h]<base:
#             rank[h],rank[l]=rank[l],rank[h]
#             l=l+1
#             break;
#         else:
#             h=h-1
#     while l<h:
#         if rank[l]>base:
#             rank[l],rank[h]=rank[h],rank[l]
#             h=h-1
#             break
#         else:
#             l=l+1
# l=left
# h=right
# print(rank)


# 将选择、冒泡、快排整理成一个模块，放在一个包里面，做成自己的库
# 详见sort.basesort
# 尝试比较一下，三个排序算法的效率
# 排序效率，快排 > 选择 >冒泡

# 写一个模块，完成以下功能：
# 	调用函数1：实现字符串反转
def reverse_str(s):
    s = s[::-1]
    print('反转后的字符串是', s)
    return s


# 	调用函数2：判断反转后字符串是否和原来字符串一模一样（返回True or False）
def same_str(s):
    s1 = reverse_str(s)
    if s1 == s:
        print('反转后与原字符相等')
        return True
    if s1 != s:
        print('反转后与原字符不相等')
        return False


# 	调用函数3：返回字符串相反的两部分
def opposite_str(s):
    s2 = s
    if same_str(s2):
        l = len(s2)
        if l % 2 == 0:
            # 长度是偶数，从中间进行截取
            print('相反的部分是', s2[:l // 2], s2[l // 2:])
        else:
            # 长度是奇数，
            print('相反的部分是', s2[:l // 2 + 1], s2[l // 2:])
    else:
        print('这个字符串没有相反的部分')


print("请输入一个字符串")
s = input()
opposite_str(s)
