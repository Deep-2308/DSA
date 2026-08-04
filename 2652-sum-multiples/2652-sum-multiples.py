class Solution:
    def sumOfMultiples(self, n):
        """
        Idea:
        - Traverse all numbers from 1 to n.
        - If a number is divisible by 3, 5, or 7, add it to the answer.
        - Return the final sum.

        Example:
        n = 7
        Multiples = 3, 5, 6, 7
        Sum = 3 + 5 + 6 + 7 = 21

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        total = 0

        for i in range(1, n + 1):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                total += i

        return total