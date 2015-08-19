"""
http://matplotlib.org/examples/pylab_examples/finance_work2.html
"""

import numpy as np

def exponentialMovingAverage(x, n):
    """
    precondition: n > len(x)
    """
    x = np.array(x)

    # initialize exponential weights
    weights = np.exp(np.linspace(-1.0, 0.0, n))
    weights /=  sum(weights)

    result = np.convolve(x, weights)[:len(x)]
    result[:n] = result[n]
    return result

def movingAverageConvergenceDivergence(x, signalTerm=9, fastTerm=12, slowTerm=26):
    slow = exponentialMovingAverage(x, slowTerm)
    fast = exponentialMovingAverage(x, fastTerm)
    signal = exponentialMovingAverage(fast - slow, signalTerm)
    return (fast - slow, signal)
