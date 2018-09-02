#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable = line-too-long
"""
    @FIle:funcs.py
    
    ~~~~~~~~~~~
    :copyright: (c) 2017 by the eigen.
    :license: BSD, see LICENSE for more details.
"""
# 一些函数式编程用到的包

from operator import mul, itemgetter, attrgetter
# mul 用来两数相乘

# itemgetter 构建一个获取字典值的函数

sample = {"a": {"b": {"c": {"d": "e"}}}}


class S(object):
    def __init__(self, v):
        self.data = v

    def __repr__(self):
        return str(self.data)


d = S(1)
d.a = S(2)
d.a.a2 = S(3)

# func = itemgetter("a", "b")
# print(func)

# print(func(sample))

func2 = attrgetter("a.a2")  # 可以获取嵌套的属性

print(func2(d))


