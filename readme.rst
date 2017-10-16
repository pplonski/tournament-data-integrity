Integrity
=========

To test the integrity of a Numerai dataset::

    $ python integrity/run.py -d numerai_dataset_20171004.zip
    INTEGRITY
      numerai_dataset_20171004.zip
    IDS
    ERAS
    REGIONS
    FEATURES
      range of feature 46 in eraX   [ 0.0000,  1.0060] not in [0, 1]
    LABELS
    PREDICTIONS
    DONE
      integrity check in 38 second

On 2017-10-04 two Numerai datasets were released. Let's run the integrity
check on the dataset that was recalled due to its strange behavior::

    $ python integrity/run.py -d numerai_dataset_20171004_problems.zip
    INTEGRITY
      numerai_dataset_20171004_problems.zip
    IDS
    ERAS
    REGIONS
    FEATURES
      range of feature  1 in eraX   [-0.0274,  1.0568] not in [0, 1]
      range of feature  2 in eraX   [ 0.0146,  1.0304] not in [0, 1]
      range of feature  3 in eraX   [ 0.0228,  1.0021] not in [0, 1]
      range of feature  4 in eraX   [-0.0239,  1.0000] not in [0, 1]
      range of feature  5 in eraX   [ 0.0092,  1.0195] not in [0, 1]
      range of feature  6 in eraX   [ 0.0000,  1.0041] not in [0, 1]
      range of feature  7 in eraX   [-0.0190,  0.9970] not in [0, 1]
      range of feature  9 in eraX   [ 0.0038,  1.0296] not in [0, 1]
      range of feature 11 in eraX   [-0.0120,  1.0039] not in [0, 1]
      range of feature 12 in eraX   [ 0.0209,  1.0134] not in [0, 1]
      range of feature 14 in eraX   [ 0.0000,  1.0091] not in [0, 1]
      range of feature 15 in eraX   [-0.0235,  0.9809] not in [0, 1]
      range of feature 16 in eraX   [-0.0511,  1.0323] not in [0, 1]
      range of feature 19 in eraX   [ 0.0000,  1.0001] not in [0, 1]
      range of feature 20 in eraX   [ 0.0107,  1.0179] not in [0, 1]
      range of feature 21 in eraX   [ 0.0000,  1.0010] not in [0, 1]
      range of feature 23 in eraX   [-0.0435,  1.0161] not in [0, 1]
      range of feature 24 in eraX   [-0.0065,  0.9911] not in [0, 1]
      range of feature 25 in eraX   [-0.0015,  0.9914] not in [0, 1]
      range of feature 27 in eraX   [ 0.0304,  1.0893] not in [0, 1]
      range of feature 28 in eraX   [-0.0191,  1.0316] not in [0, 1]
      range of feature 29 in eraX   [-0.0102,  1.0000] not in [0, 1]
      range of feature 30 in eraX   [ 0.0347,  1.0125] not in [0, 1]
      range of feature 31 in eraX   [-0.0599,  1.0000] not in [0, 1]
      range of feature 33 in eraX   [ 0.0080,  1.0420] not in [0, 1]
      range of feature 34 in eraX   [-0.0198,  1.0000] not in [0, 1]
      range of feature 35 in eraX   [-0.0047,  0.9867] not in [0, 1]
      range of feature 39 in eraX   [-0.0098,  0.9801] not in [0, 1]
      range of feature 40 in eraX   [ 0.0047,  1.0506] not in [0, 1]
      range of feature 41 in eraX   [ 0.0250,  1.0002] not in [0, 1]
      range of feature 42 in eraX   [ 0.0197,  1.0857] not in [0, 1]
      range of feature 43 in eraX   [-0.0053,  1.0101] not in [0, 1]
      range of feature 44 in eraX   [-0.0022,  1.0056] not in [0, 1]
      range of feature 45 in eraX   [ 0.0058,  1.0042] not in [0, 1]
      range of feature 47 in eraX   [-0.0208,  1.1962] not in [0, 1]
      range of feature 48 in eraX   [ 0.0148,  1.0049] not in [0, 1]
      range of feature 49 in eraX   [ 0.0045,  1.0190] not in [0, 1]
    LABELS
    PREDICTIONS
      predictions in live region [ 0.2285,  0.7889] not in [0.3719981696219426, 0.61056903427274645]
    DONE
      integrity check in 38 second

You can optionally write to a logfile and a warnfile by appending
``-l logfile.txt`` and ``-w warnfile.txt`` to the command above.

There is also a Data object which can be used like this::

    $ ipython
    In [1]: from integrity.data import Data
    In [2]: data = Data('numerai_dataset_20171004.zip')
    In [3]: data
    Out[3]:
    numerai_dataset_20171004.zip
     884553  rows
         50  features
         98  eras
          0  duplicate IDs
     0.5000  mean label
     0.0000  min feature
     0.4993  mean feature
     1.0060  max feature
     0.1172  std feature
     0.0000  min abs corr
     0.2030  mean abs corr
     0.7413  max abs corr

Requirements
============

- python
- numpy
- sklearn
- pandas

License
=======

Integrity is distributed under the Simplified BSD License.
