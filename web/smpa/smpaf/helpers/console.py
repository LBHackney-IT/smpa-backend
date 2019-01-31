# -*- coding: utf-8 -*-

"""
    helpers.console
    ~~~~~~~~~~~~~~~
    Console level logging that doesn't barf on unicode.
"""

from __future__ import absolute_import, unicode_literals

import inspect
import os

import arrow

from .colours import blue, cyan, green, magenta, orange, red, yellow  # NOQA


class Logger(object):

    def _get_code_position(self, curframe):
        frame = inspect.getouterframes(curframe, 0)
        base = os.getcwd()
        try:
            pos = '{}:{}'.format(frame[1].filename.replace(base, ''), frame[1].lineno)
        except IndexError:  # We couldn't get the stack info for some reason
            return '¯\_(ツ)_/¯'
        else:
            return pos

    def _output(self, prefix, msg, extra):
        print('{}\n> {} {}'.format(prefix, decode(msg), extra if extra else ''))

    def _ts(self):
        return magenta(str(arrow.now().format('H:mm:ss')))

    def info(self, msg, extra=None):
        """Output a message in the INFO style

        Args:
            msg (str): The message you want to output
            extra (None, optional): Anything else you want added to the message
        """
        curframe = inspect.currentframe()
        pos = self._get_code_position(curframe)
        prefix = '{} - {} - {}'.format(self._ts(), blue('INFO'), pos)
        self._output(prefix, msg, extra)

    def debug(self, msg, extra=None):
        return self.info(msg, extra)

    def log(self, msg, extra=None):
        """Output a message in the LOG style

        Args:
            msg (str): The message you want to output
            extra (None, optional): Anything else you want added to the message
        """
        curframe = inspect.currentframe()
        pos = self._get_code_position(curframe)
        prefix = '{} - {} - {}'.format(self._ts(), yellow('LOG'), pos)
        self._output(prefix, msg, extra)

    def warn(self, msg, extra=None):
        """Output a message in the WARN style

        Args:
            msg (str): The message you want to output
            extra (None, optional): Anything else you want added to the message
        """
        curframe = inspect.currentframe()
        pos = self._get_code_position(curframe)
        prefix = '{} - {} - {}'.format(self._ts(), orange('WARN'), pos)
        self._output(prefix, msg, extra)

    def error(self, msg, extra=None):
        """Output a message in the ERROR style

        Args:
            msg (str): The message you want to output
            extra (None, optional): Anything else you want added to the message
        """
        curframe = inspect.currentframe()
        pos = self._get_code_position(curframe)
        prefix = '{} - {} - {}'.format(self._ts(), red('ERROR'), pos)
        self._output(prefix, msg, extra)

    def success(self, msg, extra=None):
        """Output a message in the SUCCESS style

        Args:
            msg (str): The message you want to output
            extra (None, optional): Anything else you want added to the message
        """
        curframe = inspect.currentframe()
        pos = self._get_code_position(curframe)
        prefix = '{} - {} - {}'.format(self._ts(), green('SUCCESS'), pos)
        self._output(prefix, msg, extra)


console = Logger()  # NOQA


def decode(val):
    """Try to decode a string, and don't stop code execution if it fails.

    Args:
        val (str): Should be a string.

    Returns:
        str: Should also be a string.
    """
    if val is None or str(val) == str(''):
        return None

    if str(str(val).strip()) == str('NULL'):
        return None

    try:
        return val.decode('utf-8')
    except Exception:
        try:
            return val.decode('latin-1')
        except Exception:
            try:
                return val.decode('ascii')
            except Exception as e:
                pass

    return val
