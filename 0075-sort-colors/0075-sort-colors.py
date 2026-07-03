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

# Driver code
if __name__ == "__main__":
    nums = [2, 0, 2, 1, 1, 0]
    
    # We instantiate the class
    obj = Solution()
    
    # We call the correctly named method
    obj.sortColors(nums)
    
    # This will now successfully print [0, 0, 1, 1, 2, 2]
    print(nums)