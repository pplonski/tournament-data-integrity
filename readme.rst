Integrity
=========

To test the integrity of a Numerai dataset::

    $ python integrity/run.py -d numerai_dataset_20171004.zip
    Integrity check of numerai_dataset_20171004.zip
    interval of feature 46 [ 0.0000,  1.0060] outside of [0, 1]

You can optionally write to a logfile and a warnfile::

    $ python integrity/run.py -d numerai_dataset_20171004.zip \
      -l logfile.txt -w warnfile.txt
    Integrity check of /path/to/numerai_dataset_20171004.zip
    interval of feature 46 [ 0.0000,  1.0060] outside of [0, 1]

Let's look inside the files::
          
    $ cat logfile.txt 
    2017-05-10 15:47:39 Integrity check of /data/ni/numerai_dataset_20171004.zip
    2017-05-10 15:48:08 interval of feature 46 [ 0.0000,  1.0060] outside of [0, 1]

    $ cat warnfile.txt 
    2017-05-10 15:48:08 [check.py:18] interval of feature 46 [ 0.0000,  1.0060] outside of [0, 1]
