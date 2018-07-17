#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable = line-too-long
"""
    @FIle:extract_class.py
    
    ~~~~~~~~~~~
    :copyright: (c) 2017 by the eigen.
    :license: BSD, see LICENSE for more details.
"""


class Person(object):
    """
    origin code
    """
    def __init__(self, name, office_number, area_number):
        self.name = name
        self.office_number = office_number
        self.area_number = area_number

    def get_name(self):
        return self.name

    def get_telephone_number(self):
        return "(" + self.area_number + ")" + self.office_number

    def get_office_number(self):
        return self.office_number

    def set_office_number(self, value):
        self.office_number = value


class TelephoneNumber(object):
    """
    可以发现原来的Person承担了部分和号码有关的操作，可以将这部分的操作分解到TelephoneNumber类中
    """

    def __init__(self, office_number, area_number):
        self.office_number = office_number
        self.area_number = area_number

    def get_telephone_number(self):
        return "(" + self.area_number + ")" + self.office_number

    def get_office_number(self):
        return self.office_number

    def set_office_number(self, value):
        self.office_number = value


class PersonRefactor(object):
    """
    origin code
    """
    def __init__(self, name, office_number, area_number):
        self.name = name
        self.phone = TelephoneNumber(office_number, area_number)

    def get_name(self):
        return self.name

    def get_telephone_number(self):
        return self.phone.get_telephone_number()

    def get_office_number(self):
        return self.office_number

    def set_office_number(self, value):
        self.office_number = value
