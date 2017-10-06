import os
import logging
import time

from integrity.data import Data
from integrity.check import check


def checker(dataset_zipfile, console=True, logfile=None, warnfile=None):
    """
    Top level integrity checker of Numerai dataset.

    Parameters
    ----------
    dataset_zipfile : str
        File path of zipped Numerai dataset.
    console : bool
        Whether logging output should be sent to console / stdout.
    logfile : {str, None}, optional
        File path for logging INFO output. By default (None) no logging is
        made file.
    warnfile : {str, None}, optional
        File path for logging WARN output. By default (None) no logging is
        made file.

    Returns
    -------
    None is returned. All other output is through Python logging.
    """
    t0 = time.time()
    config_logging(console=console, logfile=logfile, warnfile=warnfile)
    logging.info("Integrity check of {}".format(dataset_zipfile))
    data = Data(dataset_zipfile)
    check(data)
    t = time.time()
    logging.info("Integrity check done in %d seconds" % (t - t0))


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


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', dest='dataset_zipfile', default=None)
    parser.add_argument('-l', dest='logfile', default=None)
    parser.add_argument('-w', dest='warnfile', default=None)
    args = parser.parse_args()
    checker(dataset_zipfile=args.dataset_zipfile,
            logfile=args.logfile,
            warnfile=args.warnfile)
