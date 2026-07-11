"""
=========================================
Problem: 1. Two Sum (Easy)
=========================================

CHEAT SHEET:
* Trigger: "Find two numbers that add up to a target", "Return their indices".
* Trap: The O(N^2) nested loop. A secondary trap is adding all numbers to the hash map *before* checking, which can accidentally use the same element twice if the target is exactly double a number. 
* Mechanism: Single-pass Hash Map.
    1. Create an empty dictionary `mp` to store {number: index}.
    2. Loop through the array using `enumerate` to get both index and value simultaneously.
    3. Calculate the required `complement` (target - current value).
    4. If the complement is already in the dictionary, you found the pair. Return the indices.
    5. Otherwise, store the current value and its index in the dictionary for future checks.

Complexity:
* Time: O(N) because we iterate once and dictionary lookups take O(1) time.
* Space: O(N) to store the dictionary.
=========================================
"""

class Solution:
    def twoSum(self, arr, target):
        mp = {}
        for i, num in enumerate(arr):
            complement = target - num
            
            if complement in mp:
                return [mp[complement], i]
                
            mp[num] = i
            
        return [-1, -1]

# ---------------------------------------
# Local Testing
# ---------------------------------------
if __name__ == "__main__":
    sol = Solution()
    arr = [2, 6, 5, 8, 11]
    target = 14

    print("Indices: {}".format(sol.twoSum(arr, target)))