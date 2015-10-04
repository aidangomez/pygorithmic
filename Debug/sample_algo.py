from Resource.algorithm import Algorithm
from Resource.enumerations import AlgorithmResponse


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
