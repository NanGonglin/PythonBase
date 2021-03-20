# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/13 14:03
@Auth ： sy 
@Function ：请输入模块功能描述
"""
#选择排序
height=[155,187,172,160,163,166,173,182,165,159]
#按升序排序
#外层，通过循环把所有剩下的人都做一次选择
for i in range (0,len(height)-1):
#记录最大元素的下标，默认第一个元素是最大的
    max=0
#从待排元素中找到最大的，放到最后
    for j in range (1,len(height)-i):
        #如果某个元素的值比最大元素的值大
        if height[j]>height[max]:
            max=j
        #把最大的元素与最后一个未排序的的元素进行交换
    height[len(height)-1-i],height[max]=height[max],height[len(height)-1-i]
    print(height)



























































