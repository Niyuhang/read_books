#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable = line-too-long
"""
    @FIle:list_comprehension.py
    
    ~~~~~~~~~~~
    :copyright: (c) 2017 by the eigen.
    :license: BSD, see LICENSE for more details.
"""

# 列表推导式

words = "abcd"
word = "hello"
codes = [ord(word) for word in words]
# 尽量保证只有一行使用，如果两行可能就要考虑用for来重写了
assert word == "hello"
# 并且在py3当中列表推导式里面的临时变量有了一个自己的局部作用域，不会影响全局的
# print(codes)





