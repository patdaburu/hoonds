#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from hoonds.errors import CustomException


class TestCustomException(CustomException):
    pass


class TestCustomExceptionSuite(unittest.TestCase):

    def test_initWithoutInner_verify(self):
        ge = TestCustomException(message='Test Message')
        self.assertEqual('Test Message', ge.message)
        self.assertIsNone(ge.inner)

    def test_initWithInner_verify(self):
        inner = Exception()
        ge = TestCustomException(message='Test Message',
                                 inner=inner)
        self.assertEqual('Test Message', ge.message)
        self.assertTrue(ge.inner == inner)