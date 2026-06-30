class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # set two pointers i and j to the start of the array
        # variable to store max profit
        # loop over the array with j. If the current value at prices[j]
        # calc the difference between the value at prices[i] and prices[j]
        # if the difference is positive, check if it is greater than the 
        # current max profit and update maxprofit if so

        # if the value at index j is less than that at index i, 
        # move pointer at i to j and continue


        maxProfit = 0
        i, j = 0, 0
        while i < len(prices):
            currentProfit = prices[j] - prices[i]
            print(currentProfit)
            maxProfit = max(maxProfit, currentProfit)
            if prices[j] < prices[i]:
                i = j

            if j != len(prices) - 1:
                j+=1
            else:
                i+=1

        return maxProfit
                    

                
