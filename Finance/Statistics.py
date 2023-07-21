
class Statistics:

    def calculate_mean(self, stock_prices):
        return sum(stock_prices) / len(stock_prices)

    def calculate_standard_deviation(self, stock_prices, sample=True):
        mean = self.calculate_mean(stock_prices)
        diffs = 0
        for stock_price in stock_prices:
            if sample:
                diffs += (stock_price - mean) ** 2 / (len(stock_prices) - 1)
            else:
                diffs += (stock_price - mean) ** 2 / len(stock_prices)
        return diffs ** .5

    def calculate_daily_returns(self, stock_prices):
        daily_returns = []
        for i in range(1, len(stock_prices)):
            daily_returns.append(stock_prices[i] / stock_prices[i-1] - 1)
        return daily_returns

    def calculate_covariance(self, stock_prices_1, stock_prices_2):
        price_length = len(stock_prices_1)
        assert(len(stock_prices_2) == price_length), "Must be given the same size prices for covariance calculation."

        diffs = 0
        mean_stock_price_1 = self.calculate_mean(stock_prices_1)
        mean_stock_price_2 = self.calculate_mean(stock_prices_2)
        for stock_price_1, stock_price_2 in zip(stock_prices_1, stock_prices_2):
            diffs += ((stock_price_1 - mean_stock_price_1) * (stock_price_2 - mean_stock_price_2))
        return diffs / (price_length - 1)

    def calculate_variance(self, stock_prices):
        return self.calculate_covariance(stock_prices, stock_prices)

    def calculate_correlation(self, stock_prices_1, stock_prices_2):
        covar = self.calculate_covariance(stock_prices_1, stock_prices_2)
        # Should this be False/True or a parameter?
        stdev_1 = self.calculate_standard_deviation(stock_prices_1, False)
        stdev_2 = self.calculate_standard_deviation(stock_prices_2, False)
        return covar / (stdev_1 * stdev_2)

    def calculate_r_squared(self, stock_prices_1, stock_prices_2):
        return self.calculate_correlation(stock_prices_1, stock_prices_2) ** 2


if __name__ == "__main__":

    test = [1, 2, 3, 4, 5]
    stats = Statistics()
    print(stats.calculate_mean(test))
    print(stats.calculate_standard_deviation(test))
    print(stats.calculate_daily_returns(test))

    stock_1 = [0.9, 1.3, 1.7, 0.4, 0.7]
    stock_2 = [2.5, 3.5, 3.6, 3.1, 2.3]
    stock_3 = [100]

    try:
        stats.calculate_covariance(stock_1, stock_3)
    except AssertionError:
        print("correctly threw exception")
        print("/n")

    print("Covariance between 1 and 2: {}".format(stats.calculate_covariance(stock_1, stock_2)))
    print("Correlation between 1 and 2: {}".format(stats.calculate_correlation(stock_1, stock_2)))


    test = "Jack"

    print(hash(test) % 7)