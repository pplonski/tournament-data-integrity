import os
import logging

import numpy as np

TAB = '  '


def config_logging(console=True, logfile=None, warnfile=None):
    """
    Set up behavior of python logging.

    Will change every package's python logging in the same session as well.
    """

    logger = logging.getLogger()
    if len(logger.handlers) > 0:
        return

    if logfile is None:
        logfile = os.devnull
    if warnfile is None:
        warnfile = os.devnull

    # log
    fmt = '%(asctime)s %(message)s'
    datefmt = '%Y-%m-%d %H:%M:%S'
    logging.basicConfig(filename=logfile, level=logging.INFO, format=fmt,
                        datefmt=datefmt)

    # warnings log
    fmt = '%(asctime)s %(message)s'
    warn = logging.FileHandler(warnfile)
    warn.setLevel(logging.WARNING)
    formatter = logging.Formatter(fmt=fmt, datefmt=datefmt)
    warn.setFormatter(formatter)
    logging.getLogger('').addHandler(warn)

    # console log
    if console:
        shell = logging.StreamHandler()
        shell.setLevel(logging.INFO)
        formatter = logging.Formatter('%(message)s')
        shell.setFormatter(formatter)
        logging.getLogger('').addHandler(shell)


def interval(message, value, limit, level='warn'):
    err_count = 0
    if value < limit[0] or value > limit[1]:
        err_count = 1
        log = get_logger(level)
        fmt = TAB + message + " %7.4f not in %s"
        log(fmt % (value, str(limit)))
    return err_count


def array_interval(message, arr, limit, level='warn'):
    err_count = 0
    amin, amax = arr.min(), arr.max()
    if amin < limit[0] or amax > limit[1]:
        err_count = 1
        log = get_logger(level)
        fmt = TAB + message + " [%7.4f, %7.4f] not in %s"
        log(fmt % (amin, amax, str(limit)))
    return err_count


def _assert(message, value, op, target, level='warn'):
    err_count = 0
    oppo = {'==': '!=',
            '!=': '==',
            '>': '<=',
            '<=': '>',
            '<': '>=',
            '>=': '<'}
    if op not in oppo:
        raise ValueError('operation `op` is not recognized')
    if op == '==':
        failed = value != target
    elif op == '!=':
        failed = value == target
    elif op == '>':
        failed = value <= target
    elif op == '<=':
        failed = value > target
    elif op == '<':
        failed = value >= target
    elif op == '<=':
        failed = value < target
    if failed:
        log = get_logger(level)
        # `value` can be a number or a str
        if type(value) == 'str' or type(value) == np.string_:
            postfix = " %s %s %s"
            value = str(value)  # in case it is a np.string_
        else:
            postfix = " %7.4f %s %s"
        fmt = TAB + message + postfix
        log(fmt % (value, oppo[op], str(target)))
    if failed:
        err_count = 1
    return err_count


def get_logger(level):
    if level == 'info':
        log = logging.info
    elif level == 'warn':
        log = logging.warn
    elif level == 'error':
        log = logging.error
    elif level == 'critical':
        log = logging.critical
    else:
        raise ValueError("logging `level` not recognized")
    return log
