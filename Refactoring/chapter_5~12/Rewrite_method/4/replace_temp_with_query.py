#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable = line-too-long
"""
    @FIle:replace_temp_with_query.py
    
    ~~~~~~~~~~~
    :copyright: (c) 2017 by the eigen.
    :license: BSD, see LICENSE for more details.
"""

class Sample(object):
    """
    origin code
    """
    __quantity = 3
    __item_price = 3.4

    def get_price(self):
        base_price = self.__item_price * self.__quantity
        discount_factor = 0.95 if base_price > 1000 else 0.98
        return base_price * discount_factor


class SampleRefactor(object):
    __quantity = 3
    __item_price = 3.4

    def get_price(self):
        return self.get_base_price() * self.get_discount_factor()

    def get_base_price(self):
        """
        通过查询方式来获取基本价格, 并且使用内联变量来使用
        """
        return self.__item_price * self.__quantity

    def get_discount_factor(self):
        discount_factor = 0.95 if self.get_base_price() > 1000 else 0.98
        return discount_factor

