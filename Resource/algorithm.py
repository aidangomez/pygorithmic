from abc import ABCMeta, abstractmethod

from Resource.enumerations import AlgorithmResponse


class Algorithm(metaclass=ABCMeta):
    def __init__(self, min_data_size=1):
        self.min_data_size = min_data_size

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Algorithm:
            if any("min_data_size" and "advise"
                   in B.__dict__ for B in C.__mro__):
                return True
        return NotImplemented

    @abstractmethod
    def advise(self, data):
        '''
        Implementation as an example only

        data - any type of data one would pass in to an algorithm (likely an
        array of price or metric data).

        precondition: data >= self.min_data_size
        returns: an AlgorithmResponse
        '''
        pass
