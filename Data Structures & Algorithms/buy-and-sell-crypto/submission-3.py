## Dynamic programming solution

# class Solution:
    # def maxProfit(self, prices: List[int]) -> int:
        
        # min_buy = prices[0]
        # max_profit = 0

        # for price in prices:
        #     profit = price - min_buy

        #     max_profit = max(max_profit, profit)

        #     min_buy = min(min_buy, price)
        
        # return max_profit

        ## Two Pointer solution

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        max_profit = 0
        
        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                max_profit = max(max_profit, profit)
            else:
                buy = sell
            
            sell += 1

        return max_profit