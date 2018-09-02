#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable = line-too-long
"""
    @FIle:decorate.py
    
    ~~~~~~~~~~~
    :copyright: (c) 2017 by the eigen.
    :license: BSD, see LICENSE for more details.
"""
# 首先装饰器会在被装饰函数被引入的时候就会执行

"""变量作用域"""

b = 9
# def foo(a):
#     # a是函数内局部作用域的， 而b则是全局作用域，这种情况没有问题
#     print(a)
#     print(b)
#
#
# foo(3)

def foo(a):
    # a是函数内局部作用域的， 而b则我们在内部先打印在进行重新赋值，这样就会出现问题
    print(a)
    print(b)
    b = 5
    # 因为在编译的时候，出现了b的赋值，而函数就认为这是一个局部变量，会从局部变量中寻找
foo(3)








