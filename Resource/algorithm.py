from abc import ABCMeta

from Resource.enumerations import AlgorithmResponse


class Algorithm(metaclass=ABCMeta):
    def __init__(self, minDataSize=1):
        self.minDataSize = minDataSize

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Algorithm:
            if any("minDataSize" and "advise"
                   in B.__dict__ for B in C.__mro__):
                return True
        return NotImplemented

    @classmethod
    @abstractmethod
    def advise(stockName, data):
        '''
        Implementation as an example only

        data - any type of data one would pass in to an algorithm (likely an
        array of price or metric data).

        precondition: data >= self.minDataSize
        returns: an AlgorithmResponse
        '''
        if (x[-1] > x[0]):
            return AlgorithmResponse.Buy
        elif (x[-1] < x[0]):
            return AlgorithmResponse.Sell
        else:
            return AlgorithmResponse.Hold
