import logging
LO = 0
HI = 1


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
    interval = [0, 1]
    for i, f in data.feature_iter():
        fmin, fmax = f.min(), f.max()
        if fmin < interval[LO] or fmax > interval[HI]:
            fmt = "interval of feature %2d [%7.4f, %7.4f] outside of %s"
            logging.warn(fmt % (i, fmin, fmax, str(interval)))


def regions(data):
    pass


def labels(data):
    pass


def predictions(data):
    pass
