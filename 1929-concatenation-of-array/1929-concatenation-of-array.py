class Solution:
    def getConcatenation(self, nums):
        """
        Idea:
        - Create a new array.
        - Traverse the original array twice.
        - Append each element during both traversals.
        - The resulting array is the concatenation of nums with itself.

        Example:
        nums = [1,2,1]

        First pass  -> [1,2,1]
        Second pass -> [1,2,1]

        Answer = [1,2,1,1,2,1]

        Time Complexity: O(n)
        Space Complexity: O(n)
        """

        ans = []

        for num in nums:
            ans.append(num)

        for num in nums:
            ans.append(num)

        return ans