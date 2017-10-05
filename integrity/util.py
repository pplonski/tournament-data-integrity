import numpy as np


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
