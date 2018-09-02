#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable = line-too-long
"""
    @FIle:func_paraments.py
    
    ~~~~~~~~~~~
    :copyright: (c) 2017 by the eigen.
    :license: BSD, see LICENSE for more details.
"""
# 使用*来接受所有未命名的定位参数，这样可以指定一些参数为关键字参数传入


def foo(a, *, b):
    # 使用* 来限定b一定要传入并且是关键字参数
    print(a, b)


print(foo.__defaults__)  # 存储一些默认值


from bobo import B