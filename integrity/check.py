import logging

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import log_loss

from integrity.util import upper_triangle, logloss_by_era
from integrity.log import interval, array_interval, _assert


def check(data):
    header(data)
    ids(data)
    eras(data)
    regions(data)
    features(data)
    labels(data)
    predictions(data)


def header(data):

    logging.info('HEADER')

    # train and tournment csv files should have the same header
    if (data.header['train'] != data.header['tournament']).any():
        logging.warn('train and tournament csv files have different headers')

    # columns should be in the correct order. We are especially concerned with
    # the order of the features which should be feature1, feature2, ... and
    # not feature1, feature10, feature11, ...
    header = ['id', 'era', 'data_type']
    header += ['feature'+str(i) for i in range(1, 51)]
    header += ['target']
    for i in range(len(header)):
        _assert('header column', data.header['train'][i], '==', header[i])

    # should have the correct number of columns
    actual = len(data.header['train'])
    desired = len(header)
    _assert('number of column in csv file', actual, '==', desired)


def ids(data):

    logging.info('IDS')

    # duplicate ids
    num_duplicate = data.ID.size - np.unique(data.ID).size
    _assert('duplicate ids', num_duplicate, '==', 0)


def eras(data):

    logging.info('ERAS')

    # number of eras
    target = {'train': 85,
              'validation': 12,
              'test': 1,
              'live': 1}
    for region in target:
        n = np.unique(data.era[data.region == region]).size
        msg = 'number of eras in %s' % region
        _assert(msg, n, '==', target[region])


def regions(data):

    logging.info('REGIONS')

    # make sure all regions are present and there are no extra regions
    target = set(['train', 'validation', 'test', 'live'])
    regions = set(np.unique(data.region))
    if regions != target:
        diff = regions - target
        if len(diff) > 0:
            logging.warn('extra regions found: %s' % str(diff))
        diff = target - regions
        if len(diff) > 0:
            logging.warn('missing regions: %s' % str(diff))


def features(data):

    logging.info('FEATURES')

    # nonfinite feature values
    n = (~np.isfinite(data.x)).sum()
    _assert('nonfinite feature values', n, '==', 0)

    # abs correlation of features
    corr = np.corrcoef(data.x.T)
    corr = upper_triangle(corr)
    corr = np.abs(corr)
    interval('mean abs corr of features', corr.mean(), [0.18, 0.22])
    interval('max  abs corr of features', corr.max(), [0.72, 0.76])

    # distribution of each feature in each era
    for era, feature_num, x in data.era_feature_iter():

        msg = 'range of feature %2d in %s' % (feature_num, era.ljust(6))
        array_interval(msg, x, [0, 1])

        msg = 'mean  of feature %2d in %s' % (feature_num, era.ljust(6))
        interval(msg, x.mean(), [0.45, 0.551])

        msg = 'std   of feature %2d in %s' % (feature_num, era.ljust(6))
        interval(msg, x.std(), [0.09, 0.15])

        msg = 'skewn of feature %2d in %s' % (feature_num, era.ljust(6))
        skew = ((x - x.mean())**3).mean() / x.std()**3
        interval(msg, skew, [-0.44, 0.44])

        msg = 'kurto of feature %2d in %s' % (feature_num, era.ljust(6))
        kurt = ((x - x.mean())**4).mean() / x.std()**4
        interval(msg, kurt, [2.45, 3.58])


def labels(data):

    logging.info('LABELS')

    # labels should only contain 0 and 1
    idx = data.nonmissing_label_index()
    y = data.y[idx]
    idx = np.logical_or(y == 0, y == 1)
    _assert("number of non 0, 1 labels", idx.size - idx.sum(), '==', 0)

    # mean of labels and number of labels
    y_mean = []
    for era, index in data.era_iter():

        y = data.y[index]

        # labels are missing in eraX
        if era != 'eraX':
            msg = 'mean of labels in %s' % era.ljust(6)
            ym = y.mean()
            interval(msg, ym, [0.499, 0.501])
            y_mean.append(ym)

        msg = 'num  of labels in %s' % era.ljust(6)
        if era == 'eraX':
            limit = [270000, 280000]
        else:
            limit = [5920, 6800]
        interval(msg, y.size, limit)

    # label bias
    msg = 'fraction of eras with label mean less than half'
    y_mean = np.array(y_mean)
    interval(msg, (y_mean < 0.5).mean(), [0.4, 0.6])


def predictions(data):

    logging.info('PREDICTIONS')

    # fit logistic regression model on train data
    idx = data.region == 'train'
    xtrain = data.x[idx]
    ytrain = data.y[idx]
    eratrain = data.era[idx]
    clf = LogisticRegression()
    clf.fit(xtrain, ytrain)

    # predict using train data
    yhat_train = clf.predict_proba(xtrain)[:, 1]

    # check train logloss and consistency
    logloss = log_loss(ytrain, yhat_train)
    interval('train logloss', logloss, [0.691, 0.693])
    loglosses = logloss_by_era(eratrain, ytrain, yhat_train)
    consistency = (loglosses < np.log(2)).mean()
    interval('train consistency', consistency, [0.57, 0.84])

    # predict using validation data
    yvalid, yhat = calc_yhat('validation', clf, data)

    # check validation logloss and consistency
    logloss = log_loss(yvalid, yhat)
    interval('validation logloss', logloss, [0.691, 0.693])
    idx = data.region == 'validation'
    loglosses = logloss_by_era(data.era[idx], yvalid, yhat)
    consistency = (loglosses < np.log(2)).mean()
    interval('validation consistency', consistency, [0.5, 0.84])

    # check test and live predictions
    for region in ('test', 'live'):
        y, yhat = calc_yhat(region, clf, data)
        target = [0.99 * yhat_train.min(), 1.01 * yhat_train.max()]
        array_interval('predictions in %s region' % region, yhat, target)


def calc_yhat(region, clf, data):
    idx = data.region == region
    x = data.x[idx]
    y = data.y[idx]
    yhat = clf.predict_proba(x)[:, 1]
    return y, yhat
