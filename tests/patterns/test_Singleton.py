#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. currentmodule:: test_Singleton
.. moduleauthor:: Pat Daburu <pat@daburu.net>
"""

import unittest
from hoonds.patterns.singleton import singleton


@singleton
class TestSingleton1(object):

    def __init__(self):
        self.foo = 0
        self.bar = "0"


class TestSingletonSuite(unittest.TestCase):

    def test_init_verifySingleInstance(self):
        original_singleton: TestSingleton1 = TestSingleton1()
        self.assertEqual(0, original_singleton.foo)
        self.assertEqual("0", original_singleton.bar)
        for i in range(1, 10):
            new_singleton = TestSingleton1()
            new_singleton.foo = i
            new_singleton.bar = str(i)
            self.assertEqual(i, original_singleton.foo)
            self.assertEqual(str(i), original_singleton.bar)