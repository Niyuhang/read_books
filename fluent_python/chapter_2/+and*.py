#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable = line-too-long
"""
    @FIle:+and*.py
    
    ~~~~~~~~~~~
    :copyright: (c) 2017 by the eigen.
    :license: BSD, see LICENSE for more details.
"""

# ==================== * 使用 ==========================
# 对序列使用*是要格外注意的地方
# 对序列进行 * 会复制里面的元素 然后 拼接起来
l = [4, 3, 2] * 5
print(l)

# 但是如果* 的是一个可变元素， 那么就要注意了
l_2 = [["_"]*3] * 3
# 第一次的 * 号得到了 ['_', '_','_']
# 然后第二次对这个列表进行 *， 这时候这三个其实都指向了同一个引用
print(l_2)

l_2[0][0] = "X"

print(l_2)

# =================== *= +=使用 ===================
# python 当中就地+ 和 就地 * 其实是调用 __iadd__ 和 __imul__方法， 如果都没有就会调用__add__ 和 __mul__
# tuple 的 *= 会返回一个新的tuple，并不是加在原来的tuple上面，而list则是直接在加在原来的列表上面
t_1 = (1, 3)
print(id(t_1))

t_1 *= 2
print(id(t_1))

l_1 = [1, 3]
print(id(l_1))

l_1 *= 2
print(id(l_1))
