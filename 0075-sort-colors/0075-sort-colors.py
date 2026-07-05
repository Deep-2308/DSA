"""
=========================================
Problem: 75. Sort Colors (Medium)
=========================================

CHEAT SHEET:
* Trigger: "Sort an array with 3 distinct values (e.g., 0, 1, 2) in-place."
* Trap: Using the built-in `.sort()` function (which takes O(N log N) time), or doing a 2-pass counting sort. 
        Interviewers specifically want this done in a SINGLE pass.
* Mechanism: The Dutch National Flag Algorithm (3 Pointers).
    1. 'low' tracks where the next 0 goes. 'high' tracks where the next 2 goes. 'mid' is the active scanner.
    2. If mid sees 0: Swap with low, increment both low and mid.
    3. If mid sees 1: It's in the right place, just increment mid.
    4. If mid sees 2: Swap with high, decrement high. (Do NOT increment mid here, the swapped number needs checking).

Complexity:
* Time: O(N) exactly one pass through the array.
* Space: O(1) strict in-place swaps.
=========================================
"""

class Solution:
    def sortColors(self, nums):
        # Initialize three pointers: low and mid at 0, high at end
        low, mid, high = 0, 0, len(nums) - 1

        # Traverse until mid crosses high
        while mid <= high:
            # If element is 0, swap with low, move both low and mid forward
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            # If element is 1, just move mid forward
            elif nums[mid] == 1:
                mid += 1
            # If element is 2, swap with high, move only high backward
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

# ---------------------------------------
# Driver Code for Local / GitHub Testing
# ---------------------------------------
if __name__ == "__main__":
    nums = [2, 0, 2, 1, 1, 0]
    
    print(f"Original Array: {nums}")
    
    # We instantiate the class and call the method
    obj = Solution()
    obj.sortColors(nums)
    
    print(f"Sorted Array:   {nums}")
