#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable = line-too-long
"""
    @FIle:extract_method.py
    
    ~~~~~~~~~~~
    :copyright: (c) 2017 by the eigen.
    :license: BSD, see LICENSE for more details.
"""


class Sample(object):
    """
    origin code
    """
    __name = "Test"
    __elements = [1.0, 2.0, 3.0, 4.4]

    def print_owing(self):
        outstanding = 0.0

        # print banner
        print("*" * 20)
        print("*" * 6 + "Customer" + "*" * 6)
        print("*" * 20)

        # calculate outstanding
        for v in self.__elements:
            outstanding += v

        # print details
        print("name:", self.__name)
        print("amount:", outstanding)


class SampleRefactor(object):
    __name = "Test"
    __elements = [1.0, 2.0, 3.0, 4.4]

    def print_owing(self):
        self.print_banner()
        outstanding = self.calculate_outstanding()
        self.print_details(outstanding)

    @staticmethod
    def print_banner() -> None:
        """
        第一类， 没有局部变量， 直接提取就好了
        """
        print("*" * 20)
        print("*" * 6 + "Customer" + "*" * 6)
        print("*" * 20)

    def print_details(self, outstanding: int) -> None:
        """
        第二类，只使用局部变量，当作参数传递
        """
        print("name:", self.__name)
        print("amount:", outstanding)

    def calculate_outstanding(self) -> int:
        """
        第三类，局部变量被使用，发现局部变量只是在外面单纯的被定义，所以直接移到函数内部定义，而如果在外部还需要计算，就当作参数传入
        """
        outstanding = 0.0
        for v in self.__elements:
            outstanding += v
        return outstanding


if __name__ == '__main__':
    sample = SampleRefactor()
    sample.print_owing()