#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable = line-too-long
"""
    @FIle:immutable_dict.py
    
    ~~~~~~~~~~~
    :copyright: (c) 2017 by the eigen.
    :license: BSD, see LICENSE for more details.
"""
# 不可变的映射类型
# 通过不可变映射 可以对字典进行限制，但是原字典的修改会影响限制类

from types import MappingProxyType

d = {"1": "A"}
d_proxy = MappingProxyType(d)

d["2"] = "B"  # 修改原字典
print(d_proxy)