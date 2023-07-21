from Statistics import Statistics
from DecayCalculator import Decay
import math


class TimeSeries:

    def calculate_log_returns(self, prices):
        log_returns = []
        for i in range(1, len(prices)):
            day_over_day = (prices[i] / prices[i-1])
            log_returns.append(math.log(day_over_day) ** 2)
        return log_returns


if __name__ == "__main__":
    ts = TimeSeries()
    stats = Statistics()

    test = [3537.06, 3537.02, 3566.74, 3595.44, 3566.15, 3598.58, 3542.53, 3542.64, 3512.42, 3544.02, 3516.32, 3542.04]
    log_returns = ts.calculate_log_returns(test)
    equal_variance = stats.calculate_variance(log_returns)

    print(Decay.calculate_decay(.94))




