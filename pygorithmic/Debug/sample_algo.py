from . import plot_graph
from ..Resource.algorithm import Algorithm
from ..Resource.enumerations import AlgorithmResponse
from ..Resource import indicators


class SampleAlgo(Algorithm):
    def advise(self, data):
        '''
        Will buy on an upward trend and sell on a downward one.
        '''
        if (data[-1] > data[0]):
            return AlgorithmResponse.buy
        elif (data[-1] < data[0]):
            return AlgorithmResponse.sell
        else:
            return AlgorithmResponse.hold


class MACDAlgo(Algorithm):
    def __init__(self, initial_data):
        super().__init__(26)
        self.stored_data = initial_data

    def advise(self, data):
        self.stored_data += data
        (macd, signal) = indicators.moving_average_convergence_divergence(
                            self.stored_data)
        macd_slope = macd[-1] - macd[-2]

        if (macd_slope > 0) & (macd[-1] < signal[-1]):
            return AlgorithmResponse.buy
        elif (macd_slope < 0) & (macd[-1] > signal[-1]):
            return AlgorithmResponse.sell
        else:
            return AlgorithmResponse.hold


class RSIAlgo(Algorithm):
    def __init__(self, initial_data):
        super().__init__(26)
        self.stored_data = initial_data

    def advise(self, data):
        self.stored_data += data
        rsi = indicators.relative_strength(self.stored_data)
        rsi_value = rsi[-1]

        if rsi_value > 70:
            return AlgorithmResponse.sell
        elif rsi_value < 30:
            return AlgorithmResponse.buy
        else:
            return AlgorithmResponse.hold


class TestAlgo(Algorithm):
    def __init__(self, initial_data):
        super().__init__(26)
        self.stored_data = initial_data

    def advise(self, data):
        self.stored_data += data
        (macd, signal) = indicators.moving_average_convergence_divergence(
                            self.stored_data)
        macd_slope = macd[-1] - macd[-2]

        rsi = indicators.relative_strength(self.stored_data)
        rsi_value = rsi[-1]

        if (rsi_value < 40) & (macd_slope > 0) & (macd[-1] < signal[-1]):
            return AlgorithmResponse.buy
        elif (rsi_value > 60) & (macd_slope < 0) & (macd[-1] > signal[-1]):
            return AlgorithmResponse.sell
        else:
            return AlgorithmResponse.hold
