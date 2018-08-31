#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable = line-too-long
"""
    @FIle:dict_sample.py
    
    ~~~~~~~~~~~
    :copyright: (c) 2017 by the eigen.
    :license: BSD, see LICENSE for more details.
"""
# defaultdict
# 其实真正实现的是default_factory 当__getitem__没有找到的时候，
# 就会调用__missing__ 这时候miss就会调用factory的
