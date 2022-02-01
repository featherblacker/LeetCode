class StockPrice(object):

    def __init__(self):
        self.timestamps = []
        self.prices = []

    def update(self, timestamp, price):
        """
        :type timestamp: int
        :type price: int
        :rtype: None
        """
        if timestamp in self.timestamps:
            index_of_timestamp = self.timestamps.index(timestamp)
            self.prices[index_of_timestamp] = price
        else:
            self.timestamps.append(timestamp)
            self.prices.append(price)

    def current(self):
        """
        :rtype: int
        """
        return self.prices[-1]

    def maximum(self):
        """
        :rtype: int
        """
        return max(self.prices)

    def minimum(self):
        """
        :rtype: int
        """
        return min(self.prices)

obj = StockPrice()
obj.update(1,10)
obj.update(2,5)
param_2 = obj.current()
param_3 = obj.maximum()
param_4 = obj.minimum()
print(param_4, param_3, param_2)

测试结果:[null,null,2308,2308,2308,2308,2308,2308,2308,2308,2308,null,7876,2308,null,7876,1866,1866,7876,null,121,7876,null,7876,7876,5339,null,5339,121,null,null,1866,1866,null,3192,null,9369,null,1006]
期望结果:[null,null,2308,2308,2308,2308,2308,2308,2308,2308,2308,null,7876,2308,null,7876,1866,1866,7876,null,121,7876,null,7876,7876,1866,null,1866,121,null,null,1866,1866,null,1866,null,9369,null,1006]