"""
=========================================
Problem: 121. Best Time to Buy and Sell Stock (Easy)
=========================================

CHEAT SHEET:
* Trigger: "Maximize profit", "choose a single day to buy and a future day to sell."
* Trap: The O(N^2) double loop checking every pair of days. 
* Mechanism: The "Min-So-Far" tracker.
    1. Initialize `mini` to the first day's price, and `maxProfit` to 0.
    2. Loop through the array.
    3. Calculate the potential profit (`cost = prices[i] - mini`).
    4. Update `maxProfit` if the current `cost` is higher.
    5. Update `mini` if the current day's price is lower than the historical `mini`.

Complexity:
* Time: O(N) single pass.
* Space: O(1) constant variables.
=========================================
"""

class Solution:
    def maxProfit(self, prices):
        # Guard clause for empty arrays
        if not prices:
            return 0
            
        mini = prices[0]
        maxProfit = 0
        
        # We can start at index 1 to avoid the redundant 0-0 math
        for i in range(1, len(prices)):
            cost = prices[i] - mini
            maxProfit = max(maxProfit, cost)
            mini = min(mini, prices[i])
            
        return maxProfit

# ---------------------------------------
# Local Testing
# ---------------------------------------
if __name__ == "__main__":
    sol = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    
    print("Maximum Profit: {}".format(sol.maxProfit(prices)))