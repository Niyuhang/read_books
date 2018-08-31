#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable = line-too-long
"""
    @FIle:bisect.py
    
    ~~~~~~~~~~~
    :copyright: (c) 2017 by the eigen.
    :license: BSD, see LICENSE for more details.
"""

# bisect 模块能够利用二分查找来在一个排序好的序列中快速找值，并且还可以很好的维护排序好的序列
# 并且可以利用里面的lo 和 hi 参数缩小范围， lo默认为0 而hi 则是默认为None 然后在开始时如果是None,会赋值为序列长度
import bisect

sorted_nums = [1, 2, 2, 4, 5, 6, 7, 8]
print(id(sorted_nums))
index_1 = bisect.bisect_left(sorted_nums, 2)  # 返回应该插入的位置，如果找到就是左侧的位置

print(index_1)

index_2_right = bisect.bisect_right(sorted_nums, 2)  # 与right 相类似，只不过返回的是插入点在右边的位置

print(index_2_right)

# ========== bisect insort ========

bisect.insort_left(sorted_nums, 3)  # 维护原有序列的插入,直接作用在原序列上
print(sorted_nums)
print(id(sorted_nums))
