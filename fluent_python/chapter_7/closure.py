#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable = line-too-long
"""
    @FIle:closure.py
    
    ~~~~~~~~~~~
    :copyright: (c) 2017 by the eigen.
    :license: BSD, see LICENSE for more details.
"""
# 闭包的关键作用在于延伸了作用域


def make_average():
    numbers = []

    def avg(num):
        # 这个numbers就是一个自由变量
        numbers.append(num)
        return sum(numbers)/len(numbers)

    return avg


avg = make_average()  # 我们调用make_average 这时候函数已经被调用，
                      # 本来作用局部变量的numbers就没了，但是因为闭包，所以numbers被绑定在了avg的__closure__中
                      # ，成了自由变量，

print(avg.__closure__)

# 这就可以用来实现装饰器当中f的传递

# 而我们改进上述的计算平均时

def make_average_v2():
    count = 0
    total = 0
    def avg(num):
        nonlocal count, total  # 跟前面出现的局部变量赋值一样，
                               # 当我们试图给一个自由变量赋值时，编译的时候就会认为这是一个局部变量而报错
        count += 1
        total += num
        return total/num

    return avg
