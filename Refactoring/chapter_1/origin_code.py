#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable = line-too-long
"""
    @FIle:origin_code.py
    
    ~~~~~~~~~~~
    :copyright: (c) 2017 by the eigen.
    :license: BSD, see LICENSE for more details.
"""

# !/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable = line-too-long
"""
    @FIle:chapter_1.py

    ~~~~~~~~~~~
    :copyright: (c) 2017 by the eigen.
    :license: BSD, see LICENSE for more details.
"""


# 原有案例

# 有一个影响租赁程序，根据租赁情况打印详单，影片有三种类型，由顾客告诉程序租赁的影片和时间，
# 然后程序返回详单。
# 金钱与 类型和时间有关
# 积分与 老片还是新片有关


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
        total_amount = 0
        frequent_renter_points = 0
        result = "Rental Record for" + self.name + "\n"
        for rental in self.__rentals:
            # 单篇影片amount计算
            tem_amount = 0
            movie = rental.movie
            if movie.price_code == "normal":
                tem_amount += 2
                if rental.days_rented > 2:
                    tem_amount += (rental.days_rented - 2) * 1.5

            elif movie.price_code == "new_release":
                tem_amount += rental.days_rented * 3

            elif movie.price_code == "children":
                tem_amount += 3
                if rental.days_rented > 3:
                    tem_amount += (rental.days_rented - 3) * 1.5
            # 积分计算
            frequent_renter_points += 1
            if movie.price_code == "new_release" and rental.days_rented > 1:
                frequent_renter_points += 1

            result += "\t" + movie.title + "\t" + str(tem_amount) + "\n"
            total_amount += tem_amount

        result += "Amount owed is" + str(total_amount) + "\n" + "you earned" + str(frequent_renter_points)
        return result

# 存在的几点问题
# 1.statement 函数无法复用，如果要输出另外类型的详单就只能再重写一个方法，而且会有比较多的重复，而这主要也是因为不符合单一职责原则，statement需要干的事情太多了
# 2.并且如果amount的计算方法或者积分的计算方法改变，或者方案无法确定时就需要进行比较多的修改


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


