class Solution:
    def twoSum(self, arr, target):
        mp = {}  # Dictionary to store element -> index
        for i, num in enumerate(arr):
            complement = target - num
            # If complement found, return indices
            if complement in mp:
                return [mp[complement], i]
            # Store current element and index
            mp[num] = i
        # No pair found
        return [-1, -1]



if __name__ == "__main__":
    sol = Solution()
    arr = [2, 6, 5, 8, 11]
    target = 14

    print(sol.twoSum(arr, target))
