from __future__ import absolute_import
import os
import time
import logging

from st2common.util import date as date_utils

__all__ = [
    'FormatNamedTimedRotatingFileHandler',
]


class FormatNamedTimedRotatingFileHandler(logging.handlers.TimedRotatingFileHandler):
    def __init__(self, filename, when='h', interval=1, backupCount=0, encoding=None, delay=False, utc=False):
        # We add aditional values to the context which can be used in the log filename
        timestamp = int(time.time())
        isotime_str = str(date_utils.get_datetime_utc_now()).replace(' ', '_')
        pid = os.getpid()
        format_values = {
            'timestamp': timestamp,
            'ts': isotime_str,
            'pid': pid
        }
        filename = filename.format(**format_values)
        super(FormatNamedTimedRotatingFileHandler, self).__init__(filename, when=when, interval=interval,
                                                                  backupCount=backupCount, encoding=encoding,
                                                                  delay=delay, utc=utc)
