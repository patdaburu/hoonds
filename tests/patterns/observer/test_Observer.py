#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. currentmodule:: tests.patterns.observer.test_Observer
.. moduleauthor:: Pat Daburu <pat@daburu.net>

Provide a brief description of the module.
"""

import unittest
from enum import Enum

from hoonds.patterns.observer import Observable, signals, SignalArguments


class TestObservable1(Observable):

    @signals()
    class Signals(Enum):
        SIGNAL_1 = "signal-1"
        SIGNAL_2 = "signal-2"

    def send_signal_1(self, args=None):
        self.send_signal(self.signals.SIGNAL_1, args)

    def send_signal_2(self, args=None):
        self.send_signal(self.signals.SIGNAL_2, args)


class TestObserver1(object):
    def __init__(self, observable: Observable):
        self.signal1_count = 0
        self.signal1_data = None
        self.signal2_count = 0
        self.signal2_data = None
        self.observable = observable
        self.observable.subscribe(self.observable.signals.SIGNAL_1, receiver=self.signal1_receiver)
        self.observable.subscribe(self.observable.signals.SIGNAL_2, receiver=self.signal2_receiver)

    def signal1_receiver(self, args: SignalArguments):
        self.signal1_count += 1
        self.signal1_data = args

    def signal2_receiver(self, args):
        self.signal2_count += 1
        self.signal2_data = args



class TestAddressRangeSuite(unittest.TestCase):

    def test_sendSignal1_verifyOnlySignal1Received(self):
        observable = TestObservable1()
        observer = TestObserver1(observable=observable)
        for i in range(0,100):
            observable.send_signal_1({'text': 'hello'})
        self.assertEqual(100,observer.signal1_count)
        self.assertEqual(0,observer.signal2_count)
        self.assertEqual('hello',observer.signal1_data['text'])

    def test_sendBothSignals_verifyBothSignalsReceived(self):
        observable = TestObservable1()
        observer = TestObserver1(observable=observable)
        for i in range(0,100):
            observable.send_signal_1()
            observable.send_signal_2()
        self.assertEqual(100,observer.signal1_count)
        self.assertEqual(100,observer.signal2_count)