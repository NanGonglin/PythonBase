# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/17 22:55
@Auth ： sy 
@Function ：请输入模块功能描述
"""
#快速排序

def quick_sort(rank,left,right):
    """
    从左往右找比基准大的，交换到h位置， h往左移动一位；再从h位置从右往左找比基准小的，
    交换到之前l的位置，l往右移动一位。反复执行前面的操作，直到l=h，因为这个时候说明
    整个列表的元素都和基准进行了比较。也就达到了基准前面的元素都比基准小，基准后面的
    元素都比基准大。当整个递归执行到列表只有一个元素的时候，就可以保证整个列表是有序的。
    :param rank: 待排序的列表，这里要用传地址
    :return:
    """
    #选取基准值,选取左边的为基准值
    base=rank[right]


    #开始的边界
    l=left
    h=right
    #一直进行操作，直到l=h
    while l<h:
        #终止条件是l=h的时候
        while l<h:
            # 从左往右找比基准大的
            if rank[l]>base:
                #把找到的元素放到h位置
                rank[l],rank[h]=rank[h],rank[l]
                #h往左移一位
                h=h-1
                #一旦找到就要停止
                break
            else:
                #如果不是，l往右移
                l+=1
        while l < h:
            # 从右往左找比基准小的
            if rank[h] < base:
                # 把找到的元素放到l位置
                rank[l], rank[h] = rank[h], rank[l]
                # l往右移一位
                l = l + 1
                # 一旦找到就要停止
                break
            else:
                # 如果不是，l往右移
                h =h- 1

    #对左边递归
    if l<=left:
        #出口
        pass
    else:
        #递归
        quick_sort(rank,left,l-1)
    # 对右边递归
    if h >= right:
        # 出口
        pass
    else:
        # 递归
        quick_sort(rank, h+1, right)

rank = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
quick_sort(rank,0,len(rank-1))
print(rank)
