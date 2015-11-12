from Resource.algorithm import Algorithm
from Resource.enumerations import AlgorithmResponse

from Resource import indicators


class SampleAlgo(Algorithm):
    def advise(self, data):
        '''
        Will buy on an upward trend and sell on a downward one.
        '''
        if (data[-1] > data[0]):
            return AlgorithmResponse.Buy
        elif (data[-1] < data[0]):
            return AlgorithmResponse.Sell
        else:
            return AlgorithmResponse.Hold


class MACDAlgo(Algorithm):
    def __init__(self, initialData):
        super().__init__(26)
        self.storedData = initialData

    def advise(self, data):
        self.storedData += data
        (MACD, signal) = indicators.movingAverageConvergenceDivergence(
                            self.storedData)
        MACDslope = MACD[-1] - MACD[-2]

        if (MACDslope > 0) & (MACD[-1] < signal[-1]):
            return AlgorithmResponse.Buy
        elif (MACDslope < 0) & (MACD[-1] > signal[-1]):
            return AlgorithmResponse.Sell
        else:
            return AlgorithmResponse.Hold


class RSIAlgo(Algorithm):
    def __init__(self, initialData):
        super().__init__(26)
        self.storedData = initialData

    def advise(self, data):
        self.storedData += data
        RSI = Resource.indicators.relativeStrength()
        RSIValue = MACD[-1]

        if RSIValue > 70:
            return AlgorithmResponse.Sell
        elif RSIValue < 30:
            return AlgorithmResponse.Buy
        else:
            return AlgorithmResponse.Hold
