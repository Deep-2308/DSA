class Solution(object):
    def maxProfit(self, prices):
        
        if not prices:
            return 0

        mini = prices[0]
        maxProfit = 0

        for i in range (1 , len(prices)):
            cost = prices[i] - mini
            maxProfit = max(maxProfit, cost)
            mini = min(mini , prices[i])

        return maxProfit


            
        