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
    for feature_num, x in data.feature_iter():
        array_interval('feature %2d' % feature_num, x, [0, 1])

    # distribution of each feature in each era
    for era, feature_num, x in data.era_feature_iter():

        msg = 'mean of feature %2d in %s' % (feature_num, era.ljust(6))
        interval(msg, x.mean(), [0.4545, 0.5505])

        msg = 'std  of feature %2d in %s' % (feature_num, era.ljust(6))
        interval(msg, x.std(), [0.09, 0.14])


def regions(data):
    pass


def labels(data):
    pass


def predictions(data):
    pass


# ---------------------------------------------------------------------------
# logging utilities

def interval(message, value, limit, level='warn'):
    if value < limit[0] or value > limit[1]:
        log = get_logger(level)
        fmt = message + " %7.4f not in %s"
        log(fmt % (value, str(limit)))


def array_interval(message, arr, limit, level='warn'):
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
