#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable = line-too-long
"""
    @FIle:class_with_call.py
    
    ~~~~~~~~~~~
    :copyright: (c) 2017 by the eigen.
    :license: BSD, see LICENSE for more details.
"""

class Chess(object):

    def __init__(self, value):
        self.value = value

    def __call__(self, *args, **kwargs):
        # 实现call方法的实例
        print("call")
        print(self.value)


chess_1 = Chess(1)
chess_1()