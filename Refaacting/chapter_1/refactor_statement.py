#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable = line-too-long
"""
    @FIle:refactor_statement.py
    
    ~~~~~~~~~~~
    :copyright: (c) 2017 by the eigen.
    :license: BSD, see LICENSE for more details.
"""

# 第一步对很长的statement函数进行重构，使得代码块变小


class Movie(object):
    """
    影片类
    """
    __title = ""
    __price_code = ""

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
    def price_code(self, value):
        self.__price_code = value


class Customer(object):
    """
    顾客
    """
    __name = ""

    def __init__(self):
        self.__rentals = []

    def add_rental(self, rental):
        self.__rentals.append(rental)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def statement(self):
        result = "Rental Record for" + self.name + "\n"
        for rental in self.__rentals:

            # 单篇影片amount计算

            tem_amount = rental.calculate_amount()
            # 积分计算
            movie = rental.movie
            result += "\t" + movie.title + "\t" + str(tem_amount) + "\n"  #

        result += "Amount owed is" + str(self.get_total_amount()) + "\n" + "you earned" + str(self.get_total_points())
        return result

    # 3 去掉临时变量total_amount， 改用查询函数去获取， 减少临时变量的存在
    def get_total_amount(self):
        result = 0
        for rental in self.__rentals:
            result += rental.calculate_amount()
        return result

    # 4 同样的方法去除frequent_renter_points
    def get_total_points(self):
        points = 0
        for rental in self.__rentals:
            points += rental.calculate_point()
        return points


class Rental(object):
    """
    租赁
    """
    __days_rented = 0

    def __init__(self, movie):
        self.__movie = movie

    @property
    def movie(self):
        return self.__movie

    @property
    def days_rented(self):
        return self.__days_rented

    @days_rented.setter
    def days_rented(self, value):
        self.__days_rented = value

    # 1 抽离出对amount的计算, 并且修改某些变量, 并且发现这个函数并没有和customer有多少关系，将代码移到rental类
    def calculate_amount(self):
        result = 0
        movie = self.movie
        if movie.price_code == "normal":
            result += 2
            if self.days_rented > 2:
                result += (self.days_rented - 2) * 1.5

        elif movie.price_code == "new_release":
            result += self.days_rented * 3

        elif movie.price_code == "children":
            result += 3
            if self.days_rented > 3:
                result += (self.days_rented - 3) * 1.5
        return result

    # 2 抽离计算积分函数
    def calculate_point(self):
        return 2 if self.movie.price_code == "new_release" \
                and self.days_rented > 1 else 1


if __name__ == '__main__':
    cus = Customer()
    cus.name = "测试"

    action_movie = Movie()
    action_movie.price_code = "normal"
    action_movie.title = "hha"

    movie_2 = Movie()
    movie_2.price_code = "new_release"
    movie_2.title = "llal"

    rental_1 = Rental(action_movie)
    rental_1.days_rented = 3
    rental_2 = Rental(movie_2)
    rental_2.days_rented = 2
    cus.add_rental(rental_1)
    cus.add_rental(rental_2)

    res = cus.statement()
    print(res)
