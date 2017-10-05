import logging

from integrity.log import log
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

    # set up behavior of python logging
    # will change any package's python logging in the same session as well
    log(console=console, logfile=logfile, warnfile=warnfile)

    logging.info("Integrity check of {}".format(dataset_zipfile))
    data = Data(dataset_zipfile)
    check(data)


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
