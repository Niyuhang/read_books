#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable = line-too-long
"""
    @FIle:array_sample.py
    
    ~~~~~~~~~~~
    :copyright: (c) 2017 by the eigen.
    :license: BSD, see LICENSE for more details.
"""
import random
import array
# 相比于之前所用的列表，当我们如果只需要一个只有数字的列表，那么用array， 也就是数组，能够进行更高效的处理
floats_generator = (random.random() for i in range(1000))  # random 会随机在[0，1）得到一个数，然后利用生成器表达式，得到1000个数

# 接着我们利用array得到一个浮点数的数组, 第一个参数表示数组中数字类型

floats = array.array("d", floats_generator)

# 还可以利用frombytes， 和 tofile 进行文件读取和存储


