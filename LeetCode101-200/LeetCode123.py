class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price, total_max_profit = float('inf'), 0
        first_profit = [0]*len(prices)
        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            total_max_profit = max(total_max_profit, prices[i]-min_price)
            first_profit[i] = total_max_profit
        max_price, max_profit = float('-inf'), 0
        for i in range(len(prices)-1, 0, -1):
            max_price = max(max_price, prices[i])
            max_profit = max(max_profit, max_price-prices[i])
            total_max_profit = max(total_max_profit, max_profit+first_profit[i-1])
        return total_max_profit


if __name__ == "__main__":
    prices = [3,3,5,0,0,3,1,4]
    max_profit = Solution().maxProfit(prices)
    print(max_profit)
