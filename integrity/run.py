import logging
import time

from integrity.data import Data
from integrity.check import check
from integrity.log import config_logging


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
    logging.info("INTEGRITY")
    logging.info("  {}".format(dataset_zipfile))
    data = Data(dataset_zipfile)
    check(data)
    t = time.time()
    logging.info("DONE")
    logging.info("  integrity check in %d second" % (t - t0))


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
