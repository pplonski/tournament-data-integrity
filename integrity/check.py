import logging


def check(data):
    ids(data)
    eras(data)
    regions(data)
    features(data)
    labels(data)
    predictions(data)


def ids(data):
    pass


def eras(data):
    pass


def features(data):

    # feature bounds
    for i, f in data.feature_iter():
        array_interval('feature %2d' % i, 'critical', f, [0, 1])


def regions(data):
    pass


def labels(data):
    pass


def predictions(data):
    pass


# ---------------------------------------------------------------------------
# logging utilities

def array_interval(message, level, arr, limit):
    amin, amax = arr.min(), arr.max()
    if amin < limit[0] or amax > limit[1]:
        log = get_logger(level)
        fmt = message + " [%7.4f, %7.4f] not in %s"
        log(fmt % (amin, amax, str(limit)))


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
