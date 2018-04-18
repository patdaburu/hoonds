#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. currentmodule:: hoonds.logging
.. moduleauthor:: Pat Daburu <pat@daburu.net>

Dear diary...
"""
from . import __version__
import deprecation
import logging


@deprecation.deprecated(deprecated_in="0.0.12", removed_in="0.1.0",
                        current_version=__version__,
                        details='Use LoggerMixin instead.')
def loggable_class(logger_name: str=None):
    """
    This is a decorator you can apply to a class to set it up with a Python ``logger`` property suitable for your
    logging needs.

    :param logger_name: a custom logger name
    :type logger_name:  ``str``

    .. note::
        If you don't supply a custom logger name, a standard formula that uses the module name and the class name
        is used.
    """
    # We need an inner function that actually adds the logger instance to the class.
    def add_logger(cls):
        # Establish what the name of the logger is going to be.  If the original caller didn't supply one, we'll use
        # a default to construct one.
        _logger_name = logger_name if logger_name is not None else '{module}.{cls}'.format(module=cls.__module__,
                                                                                           cls=cls.__name__)
        # Add a logger property to the class.
        cls.logger = logging.getLogger(_logger_name)
        return cls
    # Return the inner function.
    return add_logger


class LoggerMixin(object):
    """
    This is a mixin for classes that require a logger.
    """
    @property
    def logger(self) -> logging.Logger:
        try:
            return self.__logger__
        except AttributeError:
            logger = logging.getLogger(
                '{module}.{cls}'.format(
                    module=self.__class__.__module__,
                    cls=self.__class__.__name__))
            self.__dict__['__logger__'] = logger
            return logger
