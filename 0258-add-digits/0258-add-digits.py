class Solution:
    def addDigits(self, num):
        """
        Idea:
        - Repeatedly calculate the sum of all digits.
        - After one pass, replace the original number with the digit sum.
        - Continue until the number has only one digit.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        while num >= 10:
            digit_sum = 0

            while num > 0:
                digit_sum += num % 10
                num //= 10

            num = digit_sum

        return num