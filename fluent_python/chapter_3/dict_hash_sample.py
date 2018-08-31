#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable = line-too-long
"""
    @FIle:dict_hash_sample.py
    
    ~~~~~~~~~~~
    :copyright: (c) 2017 by the eigen.
    :license: BSD, see LICENSE for more details.
"""
# python dict的 查找
# 其实先把 search_key 进行hash, 然后根据散列表获得偏移量 然后去找散列表的值，如果找到再比对found_key和search_key 如果不一样
# 就再次进行偏移量计算 解决散裂冲突


d = {"1": "2", "2": "2", "3": "3"}

print(hash("1"))
print(hash("2"))
print(hash("3"))