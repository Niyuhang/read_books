#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable = line-too-long
"""
    @FIle:refactor_statement_2.py
    
    ~~~~~~~~~~~
    :copyright: (c) 2017 by the eigen.
    :license: BSD, see LICENSE for more details.
"""
# 在完成第一步的修改后，差不多可以复用statement了， 但是当用户需要新增影片类型，就需要进行改动，
# 并且发现calculate_amount 需要根据影片类型进行判断，这时候尽量不对其他对象的属性判断，所以将这个函数改到Movie类，
# 同时还有一个原因是为什么将这个改到Movie,传入一个租期作为变量，是因为Movie是一个改动会比较多的类，而且会新增，但是Rental并不会，所以将这个函数迁移到Movie类里面。

# 下一步思考，对于Movie类的calculate的计算看起来像是有不同的Movie子类，例如儿童类，新片类等，
# 但是一部影片在初始化好以后，例如是儿童类的实例，但是影片类是可以修改自己的类型的，但是对象是不能修改自己属于的类的，
# 这里也是因为一个影片会多次可能修改自己的类型，使用都是Movie类，而price等的属性，注入一个price的属性类，来进行控制，类似状态模式


# 对calculate就集中在Price中
class Price(object):
    @staticmethod
    def calculate_amount(days_range):
        pass


class NormalPrice(Price):
    @staticmethod
    def calculate_amount(days_range):
        result = 0
        if days_range > 2:
            result += (days_range - 2) * 1.5
        return result


class ChildrenPrice(Price):
    @staticmethod
    def calculate_amount(days_range):
        return days_range * 3


class NewReleasePrice(Price):
    @staticmethod
    def calculate_amount(days_range):
        result = 3
        if days_range > 3:
            result += (days_range - 3) * 1.5
        return result


class Movie(object):

    """
    影片类
    """
    __title = ""
    __price_code = Price()

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    @property
    def price_code(self):
        return self.__price_code

    @price_code.setter
    def price_code(self, price):
        if price == "normal":
            self.__price_code = NormalPrice()
        elif price == "children":
            self.__price_code = ChildrenPrice()
        elif price == "new_release":
            self.__price_code = NewReleasePrice()

    def calculate_amount(self, days_range):
        return self.price_code.calculate_amount(days_range)

    # 2 同样将积分函数计算放入Movie类
    def calculate_point(self, days_range):
        return 2 if self.price_code == "new_release" \
                and days_range > 1 else 1



