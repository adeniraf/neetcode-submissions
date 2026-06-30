class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            currP = prices[r] - prices[l]
            if prices[r] < prices[l]:
                l = r
                r +=1
            else:
                maxP = max(maxP, currP)
                r+=1
        return maxP


        