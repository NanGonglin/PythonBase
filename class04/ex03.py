# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/13 14:03
@Auth ： sy 
@Function ：请输入模块功能描述
"""
#冒泡排序
#取第一个数为最小的数，依次和后面紧挨的数左比较，如果比它小，交换位置，n-1次交换完成
height=[155,187,172,160,163,166,173,182,165,159]
for i in range (0,len(height)-1):
    for j in range (0,len(height)-1):
        if height[j+1]<height[j]:
            height[j],height[j+1]=height[j+1],height[j]
    print(height)































