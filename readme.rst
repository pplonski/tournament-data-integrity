Integrity
=========

To test the integrity of a Numerai dataset::

    $ python integrity/run.py -d numerai_dataset_20171004.zip
    Integrity check of numerai_dataset_20171004.zip
    interval of feature 46 [ 0.0000,  1.0060] outside of [0, 1]

You can optionally write to a logfile and a warnfile by appending
`-l logfile.txt` and `-w warnfile.txt` to the command above.

Let's look inside the files::

    $ cat logfile.txt
    2017-10-05 15:47:39 Integrity check of /data/ni/numerai_dataset_20171004.zip
    2017-10-05 15:48:08 interval of feature 46 [ 0.0000,  1.0060] outside of [0, 1]

    $ cat warnfile.txt
    2017-10-05 15:48:08 [check.py:18] interval of feature 46 [ 0.0000,  1.0060] outside of [0, 1]

There is also a Data object which can be used like this::

    $ ipython
    In [1]: from integrity.data import Data
    In [2]: data = Data('numerai_dataset_20171004.zip')
    In [3]: data
    Out[3]:
    /data/ni/numerai_dataset_20171004.zip
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
