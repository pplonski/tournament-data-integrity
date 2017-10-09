Integrity
=========

To test the integrity of a Numerai dataset::

    $ python integrity/run.py -d numerai_dataset_20171004.zip
    INTEGRITY
      /data/ni/numerai_dataset_20171004.zip
    IDS
    ERAS
    REGIONS
    FEATURES
      mean abs corr of features  0.2030 not in [0.1, 0.2]
      max  abs corr of features  0.7413 not in [0.6, 0.7]
      mean  of feature 36 in era10   0.5506 not in [0.4545, 0.5505]
      mean  of feature 36 in era11   0.5506 not in [0.4545, 0.5505]
      mean  of feature 36 in era13   0.5506 not in [0.4545, 0.5505]
      mean  of feature 36 in era14   0.5507 not in [0.4545, 0.5505]
      mean  of feature 36 in era16   0.5506 not in [0.4545, 0.5505]
      mean  of feature 36 in era19   0.5505 not in [0.4545, 0.5505]
      mean  of feature 36 in era24   0.5505 not in [0.4545, 0.5505]
      skewn of feature  4 in era29  -0.4111 not in [-0.4, 0.4]
      skewn of feature  4 in era30  -0.4358 not in [-0.4, 0.4]
      skewn of feature  4 in era31  -0.4276 not in [-0.4, 0.4]
      skewn of feature  4 in era32  -0.4061 not in [-0.4, 0.4]
      skewn of feature  4 in era34  -0.4122 not in [-0.4, 0.4]
      kurto of feature  4 in era34   3.5749 not in [2.5, 3.5]
      kurto of feature  4 in era40   3.5013 not in [2.5, 3.5]
      skewn of feature  4 in era42  -0.4202 not in [-0.4, 0.4]
      skewn of feature  4 in era45  -0.4183 not in [-0.4, 0.4]
      kurto of feature  4 in era45   3.5304 not in [2.5, 3.5]
      std   of feature 28 in era46   0.1404 not in [0.09, 0.14]
      mean  of feature 36 in era55   0.5505 not in [0.4545, 0.5505]
      std   of feature 46 in era6    0.1414 not in [0.09, 0.14]
      std   of feature 46 in era7    0.1425 not in [0.09, 0.14]
      skewn of feature  4 in era73  -0.4058 not in [-0.4, 0.4]
      skewn of feature  4 in era76  -0.4295 not in [-0.4, 0.4]
      skewn of feature  4 in era77  -0.4360 not in [-0.4, 0.4]
      skewn of feature  4 in era78  -0.4100 not in [-0.4, 0.4]
      std   of feature 46 in era8    0.1408 not in [0.09, 0.14]
      skewn of feature  4 in era86  -0.4010 not in [-0.4, 0.4]
      range of feature 46 in eraX   [ 0.0000,  1.0060] not in [0, 1]
    LABELS
      num  of labels in era25  6757.0000 not in [5940, 6750]
      num  of labels in era34  6793.0000 not in [5940, 6750]
      num  of labels in era48  5930.0000 not in [5940, 6750]
      num  of labels in era51  5934.0000 not in [5940, 6750]
      num  of labels in era54  5934.0000 not in [5940, 6750]
      num  of labels in era57  5927.0000 not in [5940, 6750]
    PREDICTIONS
    DONE
      integrity check in 38 second

You can optionally write to a logfile and a warnfile by appending
``-l logfile.txt`` and ``-w warnfile.txt`` to the command above. Let's look
inside the files::

    $ cat logfile.txt
    2017-10-06 15:19:57 INTEGRITY
    2017-10-06 15:19:57   /data/ni/numerai_dataset_20171004.zip
    2017-10-06 15:20:24 IDS
    2017-10-06 15:20:25 ERAS
    2017-10-06 15:20:25 REGIONS
    2017-10-06 15:20:25 FEATURES
    2017-10-06 15:20:25   mean abs corr of features  0.2030 not in [0.1, 0.2]
    2017-10-06 15:20:25   max  abs corr of features  0.7413 not in [0.6, 0.7]
    2017-10-06 15:20:25   mean  of feature 36 in era10   0.5506 not in [0.4545, 0.5505]
    2017-10-06 15:20:25   mean  of feature 36 in era11   0.5506 not in [0.4545, 0.5505]
    2017-10-06 15:20:25   mean  of feature 36 in era13   0.5506 not in [0.4545, 0.5505]
    2017-10-06 15:20:25   mean  of feature 36 in era14   0.5507 not in [0.4545, 0.5505]
    2017-10-06 15:20:26   mean  of feature 36 in era16   0.5506 not in [0.4545, 0.5505]
    2017-10-06 15:20:26   mean  of feature 36 in era19   0.5505 not in [0.4545, 0.5505]
    2017-10-06 15:20:26   mean  of feature 36 in era24   0.5505 not in [0.4545, 0.5505]
    2017-10-06 15:20:27   skewn of feature  4 in era29  -0.4111 not in [-0.4, 0.4]
    2017-10-06 15:20:27   skewn of feature  4 in era30  -0.4358 not in [-0.4, 0.4]
    2017-10-06 15:20:27   skewn of feature  4 in era31  -0.4276 not in [-0.4, 0.4]
    2017-10-06 15:20:27   skewn of feature  4 in era32  -0.4061 not in [-0.4, 0.4]
    2017-10-06 15:20:27   skewn of feature  4 in era34  -0.4122 not in [-0.4, 0.4]
    2017-10-06 15:20:27   kurto of feature  4 in era34   3.5749 not in [2.5, 3.5]
    2017-10-06 15:20:27   kurto of feature  4 in era40   3.5013 not in [2.5, 3.5]
    2017-10-06 15:20:28   skewn of feature  4 in era42  -0.4202 not in [-0.4, 0.4]
    2017-10-06 15:20:28   skewn of feature  4 in era45  -0.4183 not in [-0.4, 0.4]
    2017-10-06 15:20:28   kurto of feature  4 in era45   3.5304 not in [2.5, 3.5]
    2017-10-06 15:20:28   std   of feature 28 in era46   0.1404 not in [0.09, 0.14]
    2017-10-06 15:20:29   mean  of feature 36 in era55   0.5505 not in [0.4545, 0.5505]
    2017-10-06 15:20:29   std   of feature 46 in era6    0.1414 not in [0.09, 0.14]
    2017-10-06 15:20:30   std   of feature 46 in era7    0.1425 not in [0.09, 0.14]
    2017-10-06 15:20:30   skewn of feature  4 in era73  -0.4058 not in [-0.4, 0.4]
    2017-10-06 15:20:30   skewn of feature  4 in era76  -0.4295 not in [-0.4, 0.4]
    2017-10-06 15:20:30   skewn of feature  4 in era77  -0.4360 not in [-0.4, 0.4]
    2017-10-06 15:20:30   skewn of feature  4 in era78  -0.4100 not in [-0.4, 0.4]
    2017-10-06 15:20:30   std   of feature 46 in era8    0.1408 not in [0.09, 0.14]
    2017-10-06 15:20:31   skewn of feature  4 in era86  -0.4010 not in [-0.4, 0.4]
    2017-10-06 15:20:35   range of feature 46 in eraX   [ 0.0000,  1.0060] not in [0, 1]
    2017-10-06 15:20:35 LABELS
    2017-10-06 15:20:35   num  of labels in era25  6757.0000 not in [5940, 6750]
    2017-10-06 15:20:35   num  of labels in era34  6793.0000 not in [5940, 6750]
    2017-10-06 15:20:35   num  of labels in era48  5930.0000 not in [5940, 6750]
    2017-10-06 15:20:35   num  of labels in era51  5934.0000 not in [5940, 6750]
    2017-10-06 15:20:35   num  of labels in era54  5934.0000 not in [5940, 6750]
    2017-10-06 15:20:35   num  of labels in era57  5927.0000 not in [5940, 6750]
    2017-10-06 15:20:35 PREDICTIONS
    2017-10-06 15:20:35 DONE
    2017-10-06 15:20:35   integrity check in 38 second

    $ cat warnfile.txt
    2017-10-06 15:20:25   mean abs corr of features  0.2030 not in [0.1, 0.2]
    2017-10-06 15:20:25   max  abs corr of features  0.7413 not in [0.6, 0.7]
    2017-10-06 15:20:25   mean  of feature 36 in era10   0.5506 not in [0.4545, 0.5505]
    2017-10-06 15:20:25   mean  of feature 36 in era11   0.5506 not in [0.4545, 0.5505]
    2017-10-06 15:20:25   mean  of feature 36 in era13   0.5506 not in [0.4545, 0.5505]
    2017-10-06 15:20:25   mean  of feature 36 in era14   0.5507 not in [0.4545, 0.5505]
    2017-10-06 15:20:26   mean  of feature 36 in era16   0.5506 not in [0.4545, 0.5505]
    2017-10-06 15:20:26   mean  of feature 36 in era19   0.5505 not in [0.4545, 0.5505]
    2017-10-06 15:20:26   mean  of feature 36 in era24   0.5505 not in [0.4545, 0.5505]
    2017-10-06 15:20:27   skewn of feature  4 in era29  -0.4111 not in [-0.4, 0.4]
    2017-10-06 15:20:27   skewn of feature  4 in era30  -0.4358 not in [-0.4, 0.4]
    2017-10-06 15:20:27   skewn of feature  4 in era31  -0.4276 not in [-0.4, 0.4]
    2017-10-06 15:20:27   skewn of feature  4 in era32  -0.4061 not in [-0.4, 0.4]
    2017-10-06 15:20:27   skewn of feature  4 in era34  -0.4122 not in [-0.4, 0.4]
    2017-10-06 15:20:27   kurto of feature  4 in era34   3.5749 not in [2.5, 3.5]
    2017-10-06 15:20:27   kurto of feature  4 in era40   3.5013 not in [2.5, 3.5]
    2017-10-06 15:20:28   skewn of feature  4 in era42  -0.4202 not in [-0.4, 0.4]
    2017-10-06 15:20:28   skewn of feature  4 in era45  -0.4183 not in [-0.4, 0.4]
    2017-10-06 15:20:28   kurto of feature  4 in era45   3.5304 not in [2.5, 3.5]
    2017-10-06 15:20:28   std   of feature 28 in era46   0.1404 not in [0.09, 0.14]
    2017-10-06 15:20:29   mean  of feature 36 in era55   0.5505 not in [0.4545, 0.5505]
    2017-10-06 15:20:29   std   of feature 46 in era6    0.1414 not in [0.09, 0.14]
    2017-10-06 15:20:30   std   of feature 46 in era7    0.1425 not in [0.09, 0.14]
    2017-10-06 15:20:30   skewn of feature  4 in era73  -0.4058 not in [-0.4, 0.4]
    2017-10-06 15:20:30   skewn of feature  4 in era76  -0.4295 not in [-0.4, 0.4]
    2017-10-06 15:20:30   skewn of feature  4 in era77  -0.4360 not in [-0.4, 0.4]
    2017-10-06 15:20:30   skewn of feature  4 in era78  -0.4100 not in [-0.4, 0.4]
    2017-10-06 15:20:30   std   of feature 46 in era8    0.1408 not in [0.09, 0.14]
    2017-10-06 15:20:31   skewn of feature  4 in era86  -0.4010 not in [-0.4, 0.4]
    2017-10-06 15:20:35   range of feature 46 in eraX   [ 0.0000,  1.0060] not in [0, 1]
    2017-10-06 15:20:35   num  of labels in era25  6757.0000 not in [5940, 6750]
    2017-10-06 15:20:35   num  of labels in era34  6793.0000 not in [5940, 6750]
    2017-10-06 15:20:35   num  of labels in era48  5930.0000 not in [5940, 6750]
    2017-10-06 15:20:35   num  of labels in era51  5934.0000 not in [5940, 6750]
    2017-10-06 15:20:35   num  of labels in era54  5934.0000 not in [5940, 6750]
    2017-10-06 15:20:35   num  of labels in era57  5927.0000 not in [5940, 6750]

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

Requirements
============

- Python
- NumPy
- sklearn

License
=======

Integrity is distributed under the Simplified BSD License.
