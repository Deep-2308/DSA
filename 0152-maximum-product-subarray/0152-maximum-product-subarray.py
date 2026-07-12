"""
=========================================
Problem: 152. Maximum Product Subarray (Medium)
=========================================

CHEAT SHEET:
* Trigger: "find a subarray that has the largest product".
* Trap: Treating it like Kadane's Algorithm (Max Subarray Sum) and only tracking the maximum. A negative number multiplied by a negative number becomes a massive positive, so you MUST track the lowest negative number as well.
* Mechanism: Min/Max tracking with Negative Swaps.
    1. Initialize `current_max`, `current_min`, and `max_product` to the first element.
    2. Loop through the rest of the array.
    3. If the current number is negative, swap `current_max` and `current_min` (because multiplying a max by a negative makes it the min, and vice versa).
    4. Update `current_max` by taking the max of the (current number) OR (current_max * current number).
    5. Update `current_min` by taking the min of the (current number) OR (current_min * current number).
    6. Update your global `max_product`.

Complexity:
* Time: O(N) single pass.
* Space: O(1) constant variables.
=========================================
"""

class Solution:
    def maxProduct(self, nums):
        current_max = nums[0]
        current_min = nums[0]
        max_product = nums[0]

        for num in nums[1:]:
            # The Magic Key: if the number is negative, min becomes max and max becomes min
            if num < 0:
                current_max, current_min = current_min, current_max

            current_max = max(num, current_max * num)
            current_min = min(num, current_min * num)

            max_product = max(max_product, current_max)

        return max_product

# ---------------------------------------
# Local Testing
# ---------------------------------------
if __name__ == "__main__":
    sol = Solution()
    nums = [2, 3, -2, 4]
    
    print("Maximum Product: {}".format(sol.maxProduct(nums)))