#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable = line-too-long
"""
    @FIle:hash_able.py
    
    ~~~~~~~~~~~
    :copyright: (c) 2017 by the eigen.
    :license: BSD, see LICENSE for more details.
"""
# 可散列的 一个可散列的对象的哈希值是不变的

# print(hash([1, 2]))

# 字典推导式

c = {"a": 2}
d = c.copy()  # 和 copy.copy是一样的

d.update({"d": 1})
# print(c, d)
# print(d.setdefault("d", []))  # setdefault 可以用在更新一个字段的时候，可以减少对key不存在的判断
#

# 用在统计一个词的出现次数

word = "aaddccdaa"
summary = {}
# for i in word:
#     count = summary.get(i, 0)  # 常用的方法
#     count += 1
#     summary[i] = count
#
# print(summary)

for i in word:
    summary[i] = summary.setdefault(i, 0) + 1

print(summary)