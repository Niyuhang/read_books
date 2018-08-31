#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable = line-too-long
"""
    @FIle:tuple.py
    
    ~~~~~~~~~~~
    :copyright: (c) 2017 by the eigen.
    :license: BSD, see LICENSE for more details.
"""
# 元祖可以用来记录数据

# 可以用来进行嵌套数据的拆包

name, cc, pop, (x, y) = ('Tokyo', 'JP', 36.933, (35.689722, 139.691667))

print(x)


"""
 具名元祖
"""
from collections import namedtuple

City = namedtuple("city", "name cc pop")

dudu_city = City("dudu", "dupi", 303)
print(dudu_city._asdict())  # 利用asdict 可以返回一个 OrderDict

"""
不可变的tuple存了可变类型
"""
# 虽然会报错，但是因为 += 先执行了 + 然后在执行 = 所以可变类型还是改变了
t_a = (1, 2, [3, 4])
try:
    t_a[2] += [3]
except TypeError:
    print(t_a)
