#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable = line-too-long
"""
    @FIle:__init__.py.py
    
    ~~~~~~~~~~~
    :copyright: (c) 2017 by the eigen.
    :license: BSD, see LICENSE for more details.
"""

# 减少对象对系统其他部分的了解
# 尽量减少服务对象和其他系统的交互，这样子在修改的时候就可以尽量少的减少修改
# 在服务对象和其他系统部分交互的地方增加一个代理，通过代理来进行控制
