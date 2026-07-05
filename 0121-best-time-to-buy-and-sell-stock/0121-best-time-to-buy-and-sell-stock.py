"""
=========================================
Problem: 121. Best Time to Buy and Sell Stock (Easy)
=========================================

CHEAT SHEET:
* Trigger: "Maximize profit", "choose a single day to buy and a future day to sell."
* Trap: Writing a nested double loop to check every single possible buy day against every possible sell day. 
        This is an O(N^2) approach and will cause a Time Limit Exceeded (TLE) crash on large datasets.
* Mechanism: The "Min-So-Far" tracker.
    1. Traverse the array exactly once.
    2. Continuously track the absolute lowest price seen so far (`min_price`).
    3. At every step, check: "If I sold today, what is my profit?" (`price - min_price`).
    4. Update `max_profit` if this new profit beats the historical high score.

Complexity:
* Time: O(N) because we only loop through the prices array once.
* Space: O(1) because we only use two variables to track the state.
=========================================
"""

class Solution:
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)

        return max_profit

# ---------------------------------------
# Driver Code for Local / GitHub Testing
# ---------------------------------------
if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    
    print(f"Stock Prices: {prices}")
    
    # Instantiate and execute
    obj = Solution()
    max_gain = obj.maxProfit(prices)
    
    print(f"Maximum Profit: {max_gain}")
