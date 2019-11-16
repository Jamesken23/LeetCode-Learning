class Solution(object):
    # 本题还有一种更简单的方法，不需要具体求出谷底和谷峰值
    # 可以连续求解，骚操作！
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        if len(prices) <= 1:
            return max_profit
        for index in range(1, len(prices)):
            if prices[index] > prices[index-1]:
                max_profit += prices[index] - prices[index-1]
        return max_profit


if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    max_profit = Solution().maxProfit(prices)
    print(max_profit)
