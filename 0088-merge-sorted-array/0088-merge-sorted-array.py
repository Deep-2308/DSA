class Solution:
    # Merges nums2 into nums1 in-place in sorted order.
    def merge(self, nums1, m, nums2, n):
        # i: last valid element index in nums1
        i = m - 1

        # j: last index of nums2
        j = n - 1

        # k: end of nums1 array
        k = m + n - 1

        # Merge from the back to avoid overwriting
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If any elements remain in nums2, copy them
        while j >= 0:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1

        # No need to copy nums1 leftovers — already in place

# Example usage
nums1 = [1, 3, 5, 0, 0, 0]
nums2 = [2, 4, 6]
m, n = 3, 3
Solution().merge(nums1, m, nums2, n)
print(nums1)
