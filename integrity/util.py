import numpy as np
from sklearn.metrics import log_loss


def upper_triangle(a):
    "return upper triangle of square array as 1d array"
    if a.ndim != 2:
        raise ValueError("`a` must be 2d")
    n = a.shape[0]
    if n != a.shape[1]:
        raise ValueError("`a` must be square")
    s = np.empty(n * (n - 1) / 2)
    idx = 0
    for i in range(n):
        si = a[i, i + 1:]
        ni = si.size
        s[idx:idx + ni] = si
        idx += ni
    return s


def logloss_by_era(era, y, yhat):
    unique_eras = np.unique(era)
    n = unique_eras.size
    logloss = np.zeros(n)
    for i in range(n):
        idx = era == unique_eras[i]
        yi = y[idx]
        yh = yhat[idx]
        logloss[i] = log_loss(yi, yh)
    return logloss
