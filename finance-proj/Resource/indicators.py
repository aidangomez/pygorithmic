"""
Big thank you to pylab for pieces of the EMA, MACD and RSI implementations.
http://matplotlib.org/examples/pylab_examples/finance_work2.html
"""

import numpy as np


def exponentialMovingAverage(x, n):
    """
    precondition: n > len(x)
    """
    x = np.array(x)

    weights = np.exp(np.linspace(-1.0, 0.0, n))
    weights /= sum(weights)

    result = np.convolve(x, weights)[:len(x)]
    result[:n] = result[n]
    return result


def movingAverageConvergenceDivergence(x, signalTerm=9, fastTerm=12, slowTerm=26):
    slow = exponentialMovingAverage(x, slowTerm)
    fast = exponentialMovingAverage(x, fastTerm)
    signal = exponentialMovingAverage(fast - slow, signalTerm)
    return (fast - slow, signal)


def relativeStrength(x, n=14):
    deltas = np.diff(x)
    seed = deltas[:n + 1]
    up = seed[seed >= 0].sum() / n
    down = -seed[seed < 0].sum() / n
    rs = up / down
    rsi = np.zeros_like(x)
    rsi[:n] = 100. - 100. / (1. + rs)
    for i in range(n, len(x)):
        delta = deltas[i - 1]
        if delta > 0:
            upval = delta
            downval = 0.
        else:
            upval = 0.
            downval = -delta
        up = (up * (n - 1) + upval) / n
        down = (down * (n - 1) + downval) / n
        rs = up / down
        rsi[i] = 100. - 100. / (1. + rs)
    return rsi


def stochastic(x, n=14):
    x = np.array(x)
    stoch = np.zeros_like(x)
    high = np.amax(x[:n])
    low = np.amin(x[:n])
    for i in range(n, len(x)):
        if (high < x[i] and x[i - n - 1] < high):
            high = x[i]
        elif (x[i - n - 1] == high):
            high = np.amax(x[i - n:i])
        if (low > x[i] and x[i - n - 1] > low):
            low = x[i]
        elif (x[i - n - 1] == low):
            low = np.amin(x[i - n:i])
        stoch[i] = 100 * (x[i] - low) / (high - low)
    return stoch
