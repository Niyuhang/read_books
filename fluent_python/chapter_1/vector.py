#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable = line-too-long
"""
    @FIle:vector.py
    
    ~~~~~~~~~~~
    :copyright: (c) 2017 by the eigen.
    :license: BSD, see LICENSE for more details.
"""
from math import hypot


class Vector(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Vector(%r %r)" % (self.x, self.y)

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("can't add {} with vector".format(other.__class__))
        return Vector(self.x + other.x, self.y + other.y)

    def __abs__(self):
        return hypot(self.x, self.y)  # 计算向量的模

    def __bool__(self):
        return bool(abs(self))

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)


if __name__ == '__main__':
    vec_1 = Vector()
    print(vec_1 * 3)
    print(vec_1 + 3)


