#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. currentmodule:: test_SignalArgs
.. moduleauthor:: Pat Daburu <pat@daburu.net>
"""

import unittest
from hoonds.patterns.observer import SignalArgs


class TestSignalArgs(SignalArgs):
    def __init__(self, arg1: str, arg2: int):
        super().__init__({
            'arg1': arg1,
            'arg2': arg2
        })

    @property
    def arg1(self) -> str:
        return super().get('arg1');

    @property
    def arg2(self) -> str:
        return super().get('arg2');

class TestSignalArgsSuite(unittest.TestCase):

    def test_init_none_verifyProperties(self):
        sa1 = TestSignalArgs(arg1='test', arg2=100)
        self.assertEqual('test', sa1.arg1)
        self.assertEqual(100, sa1.arg2)