#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable = line-too-long
"""
    @FIle:func_partial.py
    
    ~~~~~~~~~~~
    :copyright: (c) 2017 by the eigen.
    :license: BSD, see LICENSE for more details.
"""

# 使用 func_partial 进行冻结参数, 可以基于一个函数生成一个新的函数，可以把原函数的一些参数固定
# 如果一个函数需要多个参数，但是有个参数是固定的，就可以冻结参数
from functools import partial
from operator import mul
triple = partial(mul, 3)

print(triple(4))

print(len("江淮瑞风S3欧洲版成都车展探馆 欧洲版车型更改前脸造型"))