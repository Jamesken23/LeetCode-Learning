class Solution(object):
    # 本题采用双指针法，从左至右依次遍历
    # 本题其实和接雨水题目很类似
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 定义获取的最大利润
        max_profit = 0
        if len(prices) <= 1:
            return max_profit

        # 分别定义股票的最小价格以及最高价格
        min_price = prices[0]
        max_price = 0
        for price in prices:
            max_price = max(max_price, price-min_price)
            min_price = min(min_price, price)
        return max_price

if __name__ == "__main__":
    prices = [2, 1, 4]
    max_profit = Solution().maxProfit(prices)
    print(max_profit)
