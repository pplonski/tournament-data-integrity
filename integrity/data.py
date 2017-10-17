import zipfile
import numpy as np
import pandas as pd

from integrity.util import upper_triangle

TRAIN_FILE = 'numerai_training_data.csv'
TOURN_FILE = 'numerai_tournament_data.csv'


class Data(object):

    def __init__(self, dataset_file):
        self.dataset_file = dataset_file
        data = load_dataset(dataset_file)
        self.header, self.ID, self.era, self.region, self.x, self.y = data
        self.unique_era = np.unique(self.era)
        self.unique_region = np.unique(self.region)

    def era_iter(self):
        for e in self.unique_era:
            index = self.era == e
            yield e, index

    def region_iter(self):
        for r in self.unique_region:
            index = self.region == r
            yield r, index

    def era_feature_iter(self):
        for e in self.unique_era:
            idx = self.era == e
            xi = self.x[idx]
            for i in range(xi.shape[1]):
                yield e, i, xi[:, i]

    def nonmissing_label_index(self):
        region = self.region
        index = np.logical_or(region == 'train', region == 'validation')
        return index

    def __repr__(self):
        x = []
        x.append("%s" % self.dataset_file)
        x.append("%7d  rows" % self.ID.size)
        x.append("%7d  features" % self.x.shape[1])
        x.append("%7d  eras" % np.unique(self.unique_era.size))
        dups = self.ID.size - np.unique(self.ID.size)
        x.append("%7d  duplicate IDs" % dups)
        x.append("%7.4f  mean label" % np.nanmean(self.y))
        x.append("%7.4f  min feature" % self.x.min())
        x.append("%7.4f  mean feature" % self.x.mean())
        x.append("%7.4f  max feature" % self.x.max())
        x.append("%7.4f  std feature" % self.x.std())
        corr = np.corrcoef(self.x.T)
        offcorr = np.abs(upper_triangle(corr))
        x.append("%7.4f  min abs corr" % offcorr.min())
        x.append("%7.4f  mean abs corr" % offcorr.mean())
        x.append("%7.4f  max abs corr" % offcorr.max())
        return '\n'.join(x)


def load_dataset(dataset_file):
    zf = zipfile.ZipFile(dataset_file)
    header, ID, era, region, x, y = load_csv(zf.open(TRAIN_FILE))
    header_t, ID_t, era_t, region_t, x_t, y_t = load_csv(zf.open(TOURN_FILE))
    header = {'train': header, 'tournament': header_t}
    ID = np.concatenate((ID, ID_t))
    era = np.concatenate((era, era_t))
    region = np.concatenate((region, region_t))
    x = np.concatenate((x, x_t))
    y = np.concatenate((y, y_t))
    return header, ID, era, region, x, y


def load_csv(file_like):
    # load data as np.array
    a = pd.read_csv(file_like, header=0)
    header = a.columns.values
    a = a.values

    # convert arrays from object dtype
    ID = a[:, 0].astype(str)
    era = a[:, 1].astype(str)
    region = a[:, 2].astype(str)
    x = a[:, 3:-1].astype(np.float64)
    y = a[:, -1]
    y[y == ''] = np.nan
    y = y.astype(np.float64)

    return header, ID, era, region, x, y
