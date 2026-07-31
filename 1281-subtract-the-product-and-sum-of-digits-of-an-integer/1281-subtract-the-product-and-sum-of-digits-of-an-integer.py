class Solution:
    def subtractProductAndSum(self, n):
        """
        Idea:
        - Traverse each digit of the number once.
        - Simultaneously calculate:
            1. Product of all digits.
            2. Sum of all digits.
        - Return (product - sum).

        Example:
        234
        Product = 2 * 3 * 4 = 24
        Sum = 2 + 3 + 4 = 9
        Answer = 24 - 9 = 15

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        product = 1
        digit_sum = 0

        while n > 0:
            digit = n % 10
            product *= digit
            digit_sum += digit
            n //= 10

        return product - digit_sum