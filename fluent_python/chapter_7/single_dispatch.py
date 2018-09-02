#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable = line-too-long
"""
    @FIle:single_dispatch.py
    
    ~~~~~~~~~~~
    :copyright: (c) 2017 by the eigen.
    :license: BSD, see LICENSE for more details.
"""
# 利用single_dispatch将函数变为分函数,根据不同变量处理
from functools import singledispatch


@singledispatch
def run_for_diff_args(html):
    return html


@run_for_diff_args.register(str)
def _(html):
    print("it's str")

#
@run_for_diff_args.register(int)
def _(html):
    print("it's int")


c = run_for_diff_args(22)
