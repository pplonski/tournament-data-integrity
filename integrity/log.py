"integrity logging"

import logging
import os

LOG_LEVEL_FILE = logging.INFO
LOG_LEVEL_STDERR = logging.INFO


def log(console=True, logfile=None, warnfile=None):

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
    logging.basicConfig(filename=logfile, level=LOG_LEVEL_FILE, format=fmt,
                        datefmt=datefmt)

    # warnings log
    fmt = '%(asctime)s [%(filename)s:%(lineno)d] %(message)s'
    warn = logging.FileHandler(warnfile)
    warn.setLevel(logging.WARNING)
    formatter = logging.Formatter(fmt=fmt, datefmt=datefmt)
    warn.setFormatter(formatter)
    logging.getLogger('').addHandler(warn)

    # console log
    if console:
        shell = logging.StreamHandler()
        shell.setLevel(LOG_LEVEL_STDERR)
        formatter = logging.Formatter('%(message)s')
        shell.setFormatter(formatter)
        logging.getLogger('').addHandler(shell)
