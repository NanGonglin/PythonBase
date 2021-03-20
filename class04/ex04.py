# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/13 14:03
@Auth ： sy 
@Function ：请输入模块功能描述
"""
# #杨辉三角
yh = 5
# #定义0次方
# arr1=[1]
# arr2=[1]
# for i in range (1,yh+1):
#     arr2.append(1)
#     for j in range (i+1):
#         if j==0 or j==len(arr2)-1:
#             arr2[j]=1
#         else:
#             arr2[j]=arr1[j-1]+arr1[j]
#     arr1=arr2.copy()
#     print(arr2)

# 定义0次方
arr1 = [1]
print('%*s' % (3 * yh, ''),end='')
print('%6d' % arr1[0])
arr2 = [1]
# 次方是从0开始，所以要加1
for i in range(1, yh + 1):
    # 从0次方推1次方
    # 增加一个系数
    arr2.append(1)
    # 计算第几次方，系数比次方多一
    for j in range(i + 1):
        # 如果是第一个元素或者最后一个元素，值为1
        if j == 0 or j == len(arr2) - 1:
            arr2[j] = 1
        else:
            # 其他元素的值等于，它肩膀上两个数之和
            arr2[j] = arr1[j - 1] + arr1[j]
    print('%*s' % (3 * (yh - i), ''), end='')
    for k in arr2:
        print('%6d' % k,end='')
    print()
    # 把arr2的系数作为arr1的系数
    arr1 = arr2.copy()
