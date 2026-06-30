class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        i, j = 0, 0
        maxP = 0

        for i in range(len(prices)):
            for j in range(i, len(prices)):
                curr_profit = prices[j] - prices[i]
                maxP = max(curr_profit, maxP)
                print(curr_profit)

        return maxP

        