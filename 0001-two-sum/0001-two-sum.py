"""
=========================================
Problem: 1. Two Sum (Easy)
=========================================

CHEAT SHEET:
* Trigger: "find two numbers that add up to target", "return indices".
* Trap: Using a nested double loop. It works, but it runs in O(N^2) time. Interviewers will immediately ask for the O(N) follow-up.
* Mechanism (Brute Force): 
    1. Loop through the array with pointer `i`.
    2. Loop through the rest of the array with pointer `j`.
    3. If nums[i] + nums[j] == target, return [i, j].

Complexity:
* Time: O(N^2) because for every element, we scan the rest of the array.
* Space: O(1) no extra memory used.
=========================================
"""

class Solution:
    def twoSum(self, nums, target):
        n = len(nums)
        
        # lock in the first number
        for i in range(n):
            # scan the rest of the array for its pair
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
                    
        return []

# ---------------------------------------
# Local Testing
# ---------------------------------------
if __name__ == "__main__":
    sol = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    
    print("Indices: {}".format(sol.twoSum(nums, target)))