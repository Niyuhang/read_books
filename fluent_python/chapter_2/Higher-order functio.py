#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable = line-too-long
"""
    @FIle:Higher-order functio.py
    
    ~~~~~~~~~~~
    :copyright: (c) 2017 by the eigen.
    :license: BSD, see LICENSE for more details.
"""
words = "abcdefg"

# 常用的高阶函数
# 1 map
codes_by_map = list(map(ord, words))  # 对可迭代对象的每一个元素进行操作
print(codes_by_map)

# 2 filter
# 对可迭代对象的每一个元素进行判断，找出所有符合规则的
codes_by_filter = list(filter(lambda x: x >= 99, codes_by_map))
print(codes_by_filter)

# reduce
# 对可迭代对象进行操作，将前两个按照函数操作后，作为值和下一个继续进行操作
from functools import reduce
value_by_codes = reduce(lambda x, y: x*y, codes_by_map)
print(value_by_codes)
