#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable = line-too-long
"""
    @FIle:set_sample.py
    
    ~~~~~~~~~~~
    :copyright: (c) 2017 by the eigen.
    :license: BSD, see LICENSE for more details.
"""
# 直接使用字面方法去创建 会比使用构造方法快
from dis import dis
dis('{1}')

dis('set([1])')

d = {"a": "b"}
a = frozenset(d)
