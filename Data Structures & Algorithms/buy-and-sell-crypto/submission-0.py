class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy = prices[0]
        max_profit = 0

        for price in prices[1:]:
            profit = price - buy

            max_profit = max(max_profit, profit)

            buy = min(buy, price)
        
        return max_profit
