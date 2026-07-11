"""
=========================================
Problem: 1. Two Sum (Variant: Two Pointers / Sorted)
=========================================

CHEAT SHEET:
* Trigger: "Array is already sorted and find two numbers that sum to target", or "Two Sum II".
* Trap: Using this approach on an UNSORTED array when you need original indices! Sorting an unsorted array takes O(N log N) time and storing index tuples takes O(N) space, making it strictly slower than a single-pass Hash Map O(N).
* Mechanism: The Two-Pointer Inward Crunch.
    1. Place the `left` pointer at index 0 and the `right` pointer at the last index.
    2. Calculate `current_sum = arr[left] + arr[right]`.
    3. If `current_sum == target`, you found the winning pair!
    4. If `current_sum < target`, the sum is too small. Move the `left` pointer one step right to grab a larger number.
    5. If `current_sum > target`, the sum is too big. Move the `right` pointer one step left to grab a smaller number.
    6. Repeat until the pointers cross.

Complexity:
* Time: O(N log N) if unsorted due to sorting; strictly O(N) if the input array is already sorted!
* Space: O(N) to store index tuples; strictly O(1) if already sorted and values are returned directly.
=========================================
"""

class Solution:
    def twoSum(self, arr, target):
        # Create list of tuples (value, original_index) to preserve indices
        nums_with_index = [(num, idx) for idx, num in enumerate(arr)]
        
        # Sort based strictly on the integer values
        nums_with_index.sort(key=lambda x: x[0])

        left = 0
        right = len(arr) - 1
        
        while left < right:
            current_sum = nums_with_index[left][0] + nums_with_index[right][0]
            
            if current_sum == target:
                return [nums_with_index[left][1], nums_with_index[right][1]]
            elif current_sum < target:
                # Sum too small -> increment left pointer to increase total
                left += 1
            else:
                # Sum too large -> decrement right pointer to decrease total
                right -= 1
                
        return [-1, -1]

# ---------------------------------------
# Local Testing
# ---------------------------------------
if __name__ == "__main__":
    sol = Solution()
    arr = [2, 6, 5, 8, 11]
    target = 14

    print("Indices found via Two-Pointer: {}".format(sol.twoSum(arr, target)))