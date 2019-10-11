# -*- coding: utf-8 -*-

"""
    helpers.console
    ~~~~~~~~~~~~~~~
    Console level logging that doesn't barf on unicode.
"""

from __future__ import absolute_import, unicode_literals

import inspect
import os
import sys
import math

import logging
import socket
from logging.handlers import SysLogHandler

import arrow
import bugsnag
from bugsnag.handlers import BugsnagHandler

from .colours import bg_blue, blue, cyan, green, magenta, orange, red, yellow  # NOQA

CONSOLE_LOG_LEVEL = 'INFO'
CLEAR = '\033[K'
HIDE_CURSOR = '\033[?25l'
SHOW_CURSOR = '\033[?25h'


LOG_LEVELS = {
    'DEBUG': 0,
    'INFO': 1,
    'SUCCESS': 2,
    'TEMPLATE': 3,
    'WARN': 4,
    'ERROR': 5
}


#################################
# PAPERTRAIL LOGGING
#################################


# class ContextFilter(logging.Filter):
#     hostname = socket.gethostname()

#     def filter(self, record):
#         record.hostname = ContextFilter.hostname
#         return True


# syslog = SysLogHandler(address=('logs6.papertrailapp.com', 43291))  # HACTAR
# # syslog = SysLogHandler(address=('logs7.papertrailapp.com', 51346))  # HACKNEY
# syslog.addFilter(ContextFilter())

# format = '%(asctime)s %(hostname)s SMPA-API: %(message)s'
# formatter = logging.Formatter(format, datefmt='%b %d %H:%M:%S')
# syslog.setFormatter(formatter)
# papertrail = logging.getLogger()
# papertrail.addHandler(syslog)
# papertrail.setLevel(logging.DEBUG)
# papertrail.info("This is a message")


####################################################################################################
# BUGSNAG LOGGING
####################################################################################################


bugsnag.configure(
    api_key=os.environ.get('BUGSNAG_API_KEY'),
    project_root=os.environ.get('BUGSNAG_PROJECT_ROOT'),
    release_stage=os.environ.get('SERVER_ENV'),
    use_ssl=True
)


bslogger = logging.getLogger("test.logger")
handler = BugsnagHandler()
# send only WARN-level logs and above
handler.setLevel(logging.WARN)
bslogger.addHandler(handler)


####################################################################################################
# CONSOLE LOGGING
####################################################################################################


class Logger(object):

    def __init__(self):
        self.spinning = False
        self.terminal = sys.stdout
        self.writing_progress = False

    def reset(self):
        self.writing_progress = False
        self.terminal.write('\r\n{}'.format(SHOW_CURSOR))
        self.terminal.flush()

    def _check_log_level(self, called_level: str) -> bool:
        """Check whether we want to actually output this message.

        Args:
            called_level (str): The level of the calling function - INFO, SUCCESS, WARN or ERROR

        Returns:
            bool: Whether we should output the message
        """
        try:
            level_str = CONSOLE_LOG_LEVEL
        except Exception:
            level_str = 'WARN'
        level = LOG_LEVELS[level_str]
        called = LOG_LEVELS[called_level]
        if called >= level:
            return True
        else:
            return False

    @staticmethod
    def _get_code_position(curframe):
        frame = inspect.getouterframes(curframe, 0)
        base = os.getcwd()
        try:
            pos = '{}:{}'.format(frame[1].filename.replace(base, ''), frame[1].lineno)
        except IndexError:  # We couldn't get the stack info for some reason
            return '¯\\_(ツ)_/¯'
        else:
            return pos

    @staticmethod
    def _output(prefix, msg, extra):
        print('{}\n> {} {}'.format(prefix, decode(msg), extra if extra else ''))

    @staticmethod
    def _ts():
        return magenta(str(arrow.now().format('H:mm:ss')))

    def info(self, msg, extra=None):
        """Output a message in the INFO style

        Args:
            msg (str): The message you want to output
            extra (None, optional): Anything else you want added to the message
        """
        if not self._check_log_level('INFO'):
            return False
        curframe = inspect.currentframe()
        pos = self._get_code_position(curframe)
        prefix = '{} - {} - {}'.format(self._ts(), blue('INFO'), pos)
        from smpa.app import config
        if config.DEBUG:
            self._output(prefix, msg, extra)
        else:
            papertrail.info(f'{prefix} - {msg} - {extra}')

    def debug(self, msg, extra=None):
        if not self._check_log_level('DEBUG'):
            return False
        return self.info(msg, extra)

    def log(self, msg, extra=None):
        """Output a message in the LOG style

        Args:
            msg (str): The message you want to output
            extra (None, optional): Anything else you want added to the message
        """
        if not self._check_log_level('DEBUG'):
            return False
        curframe = inspect.currentframe()
        pos = self._get_code_position(curframe)
        prefix = '{} - {} - {}'.format(self._ts(), yellow('LOG'), pos)
        from smpa.app import config
        if config.DEBUG:
            self._output(prefix, msg, extra)
        else:
            papertrail.info(f'{prefix} - {msg} - {extra}')

    def warn(self, msg, extra=None):
        """Output a message in the WARN style

        Args:
            msg (str): The message you want to output
            extra (None, optional): Anything else you want added to the message
        """
        if not self._check_log_level('WARN'):
            return False
        curframe = inspect.currentframe()
        pos = self._get_code_position(curframe)
        prefix = '{} - {} - {}'.format(self._ts(), orange('WARN'), pos)
        from smpa.app import config
        if config.DEBUG:
            self._output(prefix, msg, extra)
        else:
            papertrail.warn(f'{prefix} - {msg} - {extra}')

    def error(self, msg, extra=None):
        """Output a message in the ERROR style

        Args:
            msg (str): The message you want to output
            extra (None, optional): Anything else you want added to the message
        """
        if not self._check_log_level('ERROR'):
            return False
        curframe = inspect.currentframe()
        pos = self._get_code_position(curframe)
        prefix = '{} - {} - {}'.format(self._ts(), red('ERROR'), pos)
        from smpa.app import config
        if config.DEBUG:
            self._output(prefix, msg, extra)
        else:
            papertrail.error(f'{prefix} - {msg} - {extra}')

    def success(self, msg, extra=None):
        """Output a message in the SUCCESS style

        Args:
            msg (str): The message you want to output
            extra (None, optional): Anything else you want added to the message
        """
        if not self._check_log_level('DEBUG'):
            return False
        curframe = inspect.currentframe()
        pos = self._get_code_position(curframe)
        prefix = '{} - {} - {}'.format(self._ts(), green('SUCCESS'), pos)
        from smpa.app import config
        if config.DEBUG:
            self._output(prefix, msg, extra)
        else:
            papertrail.info(f'{prefix} - {msg} - {extra}')

    def progress(self, msg='', perc=0, demo=False):
        message = blue(msg)
        self.terminal.write('\r{}'.format(CLEAR))
        self.terminal.flush()
        blocks = math.floor(perc / 5)
        spaces = math.ceil((100 - perc) / 5)
        perc = "{0:.2f}".format(perc)
        self.terminal.write(
            ' [{}{}] {}% {}\r'.format(bg_blue(' ') * blocks, ' ' * spaces, perc, message)
        )
        self.terminal.flush()
        self.writing_progress = True


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

