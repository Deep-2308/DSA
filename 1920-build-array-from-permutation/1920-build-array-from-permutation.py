class Solution:
    def buildArray(self, nums):
        """
        Idea:
        - Create a new array of the same size.
        - For each index i, the required value is nums[nums[i]].
        - Store this value in the answer array and return it.

        Example:
        nums = [0,2,1,5,3,4]

        ans[0] = nums[nums[0]] = nums[0] = 0
        ans[1] = nums[nums[1]] = nums[2] = 1
        ans[2] = nums[nums[2]] = nums[1] = 2
        ...

        Answer = [0,1,2,4,5,3]

        Time Complexity: O(n)
        Space Complexity: O(n)
        """

        ans = []

        for i in range(len(nums)):
            ans.append(nums[nums[i]])

        return ans