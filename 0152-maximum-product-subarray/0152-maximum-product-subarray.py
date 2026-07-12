class Solution:
    def maxProduct(self, nums):
        current_max = nums[0]
        current_min = nums[0]
        max_product = nums[0]

        for num in nums[1:]:
            if num < 0:
                current_max, current_min = current_min, current_max

            current_max = max(num, current_max * num)
            current_min = min(num, current_min * num)

            max_product = max(max_product, current_max)

        return max_product