#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable = line-too-long
"""
    @FIle:remove_method.py
    
    ~~~~~~~~~~~
    :copyright: (c) 2017 by the eigen.
    :license: BSD, see LICENSE for more details.
"""


class AccountType(object):

    @property
    def is_premium(self):
        return False


class AccountTypeA(AccountType):
    pass


class AccountTypeB(AccountType):
    @property
    def is_premium(self):
        return True


class Account(object):
    """
    origin code
    """
    def __init__(self, acc_type, days_overdrawn):
        self.acc_type = acc_type
        self.days_overdrawn = days_overdrawn

    def overdraft_charge(self):
        """
        透支金额计算
        """
        if self.acc_type.is_premium:
            result = 10
            if self.days_overdrawn > 7:
                result += (self.days_overdrawn - 7) * 0.85
                return result
        else:
            return self.days_overdrawn * 1.75

    def bank_charge(self):
        result = 4.5
        if self.days_overdrawn > 0:
            result += self.overdraft_charge()
        return result


class AccountType(object):
    @property
    def is_premium(self):
        return False

    def overdraft_charge(self, days_overdrawn):
        """
        透支金额计算
        """
        if self.is_premium:
            result = 10
            if days_overdrawn > 7:
                result += (days_overdrawn - 7) * 0.85
                return result
        else:
            return days_overdrawn * 1.75


class AccountRefactor(object):
    """
    重构后的Account
    """
    # 思考每个账号类型会有自己的透支算法，所以透支算法应该放到AccountType类里面，在看days_overdrawn ，是否应该迁移过去，
    # 应该这个参数与Account是有关系的，不同账号数量不同，所以留在原来类当中,同时如果传入参数与原来类关联比较大，可以把原有类的对象传入

    def __init__(self, acc_type, days_overdrawn):
        self.acc_type = acc_type
        self.days_overdrawn = days_overdrawn

    def overdraft_charge(self):
        """
        透支金额计算
        """
        return self.acc_type.overdraft_charge(self.days_overdrawn)

    def bank_charge(self):
        result = 4.5
        if self.days_overdrawn > 0:
            result += self.overdraft_charge()
        return result
