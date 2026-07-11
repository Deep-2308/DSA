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
        # Store each number with its original index
        # Example:
        # arr = [2, 6, 5, 8, 11]
        # nums_with_index = [(2,0), (6,1), (5,2), (8,3), (11,4)]
        nums_with_index = [(num, idx) for idx, num in enumerate(arr)]

        # Sort the list by the number (first element of each tuple)
        # After sorting:
        # [(2,0), (5,2), (6,1), (8,3), (11,4)]
        nums_with_index.sort(key=lambda x: x[0])

        # Two pointers
        left = 0
        right = len(arr) - 1

        # Keep checking until the pointers meet
        while left < right:

            # Current sum of the left and right values
            current_sum = (
                nums_with_index[left][0] +
                nums_with_index[right][0]
            )

            # If the target is found, return the ORIGINAL indices
            if current_sum == target:
                return [
                    nums_with_index[left][1],
                    nums_with_index[right][1]
                ]

            # Sum is too small
            # Move left pointer right to increase the sum
            elif current_sum < target:
                left += 1

            # Sum is too large
            # Move right pointer left to decrease the sum
            else:
                right -= 1

        # No pair found
        return [-1, -1]


# -------------------------
# Local Testing
# -------------------------
if __name__ == "__main__":
    sol = Solution()

    arr = [2, 6, 5, 8, 11]
    target = 14

    print(sol.twoSum(arr, target))