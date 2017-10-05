import logging

from log import log


def check(dataset_file, console=True, logfile=None, warnfile=None):
    """
    Top level integrity checker of Numerai dataset.

    Parameters
    ----------
    dataset_file : str
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

    log(console=console, logfile=logfile, warnfile=warnfile)

    logging.info("Integrity check of {}".format(dataset_file))


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', dest='dataset_file', default=None)
    args = parser.parse_args()
    check(dataset_file=args.dataset_file)
