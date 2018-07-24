import numpy as np
from numpy import random

"""
This module is just a collection of code to be used in conjunction with chapter 4. Enjoy!
"""


def holes(data, ratio=0.1, seed=None):
    """
    a function that, pseudo-randomly, pokes holes into a dataset.
    Parameters:
        @data - a 2D numpy array of data in the form of Scikit-learn datasets.
           size = ['number of samples','number of features']
        @ratio - desired ratio of deleted datapoints to untouched datapoints
        @seed -  a seed to be fed into the random number generator for repeatability
    """

    samples = len(data)
    features = len(data[0])
    random.seed(seed)
    # make an array of random numbers between 0 and 1
    rand = random.rand(samples, features)
    # find the indeces of this array that are below the threshold set by ratio
    erase = np.nonzero(rand < ratio)
    # set the data at the values below the threshold to zero
    data[erase] = None
    return data
