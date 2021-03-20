# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/20 14:07
@Auth ： sy 
@Function ：请输入模块功能描述
"""
import time


def dec_time(params):
    """
    定义装饰器
    :param params: 装饰器本身的函数
    :return:
    """

    def get_func(func):
        """
        获取使用了装饰器的函数
        :param func: 运行，并使用了装饰器的函数
        :return:
        """

        def wrapper(*args, **kwargs):
            """

            :param args: 运行的函数的位置型参数
            :param kwargs: 运行的函数的可变参数
            :return:
            """
            # print(params)
            # print(func.__name__)
            # print(args)
            # print(kwargs)

            # 可以在函数运行前，添加代码,快速导包，alt+tab键
            start = time.time()
            # 调用函数本身，参数按原样传递
            res = func(*args, **kwargs)
            # 也可以在函数运行后，添加代码
            end = time.time()
            if params == 'ms':
                print("函数：%s运行耗时%5.2fms" % (func.__name__, (end - start) * 1000))
            else:
                print("函数：%s运行时间耗时%5.2fs" % (func.__name__, end - start))

            return res

        return wrapper

    return get_func


@dec_time('ms')
def my_funcn(a, b, c=1, d=1):
    time.sleep(1)
    print("执行函数本身")


if __name__ == '__main__':
    a = my_funcn(1, 2, c=3, d=4)
    print(a)
