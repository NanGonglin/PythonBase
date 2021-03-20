# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/16 20:18
@Auth ： sy 
@Function ：请输入模块功能描述
"""
import class05.ex02

# 函数
# 字符串的替换，想替换第n个字符串
def replace_sub(s, n, old, new):
    """
    给定一个字符串，想替换第n个字符串
    :param s: 给定的字符串
    :param n: 需要替换的第几个字符串
    :param old: 需要替换的字符
    :param new:替换的新的字符
    :return:返回替换后新的字符串
    """
    if s.count(old) < 5:
        # return结束函数的运行,后面的都不执行
        return s
    # 前n个都替换为最新的字符
    s = s.replace(old, new, n)
    # 前n-1个替换回原来的值
    s = s.replace(new, old, n - 1)
    return s
def test():
    print("测试一下")

#只有把这个py文件作为运行文件的时候，才执行下面的代码，被导入该模块的时候是不执行下面这段代码的
if __name__=='__main__':
    print(replace_sub.__doc__)

    s = 'adefuadnerceadwguewadfowe'
    s = replace_sub(s, 4, 'ad', 'sr')
    print(s)
