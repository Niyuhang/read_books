#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable = line-too-long
"""
    @FIle:slice.py
    
    ~~~~~~~~~~~
    :copyright: (c) 2017 by the eigen.
    :license: BSD, see LICENSE for more details.
"""

# python 当中很常有的切片操作

words = "abcdefg"

word = words[1:4:2]  # 表示从index 1 到 4 不包括4 不包括最后一个是因为从序列0开始，并且可以根据自己想要的直接计算应该到哪里结束
                     # 2表示间隔两个位置

print(word)

word_reserve = words[::-1]  # 负号间隔就表示倒着取
print(word_reserve)

# 再切片当中就算超出了原来的长度也不会报错


