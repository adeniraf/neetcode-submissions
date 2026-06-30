class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low, high = 0, 0 
        max_profit = 0

        while high <= len(prices) - 1:
            curr_profit = prices[high] - prices[low]
            if prices[high] >= prices[low]:
                high += 1
            else:
                low = high
            max_profit = max(curr_profit, max_profit)
        return max_profit