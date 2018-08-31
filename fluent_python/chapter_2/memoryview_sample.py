#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable = line-too-long
"""
    @FIle:memoryview_sample.py
    
    ~~~~~~~~~~~
    :copyright: (c) 2017 by the eigen.
    :license: BSD, see LICENSE for more details.
"""
# 内存视图
# 可以让用户操作同一个数组的不同切片，直接不需要复制就可以操作同一个内存
import array

a = array.array("d", [1.2333, 2.3333, 3.333333])

memv = memoryview(a)

memv[0] = 1.333

print(a)


