class Solution:
    def isSameAfterReversals(self, num):
        """
        Idea:
        - A number loses its trailing zeros after the first reversal.
        - If the original number ends with 0 (except 0 itself),
          the second reversal cannot restore those zeros.
        - Therefore:
            * Return True if num == 0 or num does not end with 0.
            * Otherwise, return False.

        Example:
        526  -> 625 -> 526  (True)
        1800 -> 81  -> 18   (False)
        0    -> 0   -> 0    (True)

        Time Complexity: O(1)
        Space Complexity: O(1)
        """

        return num == 0 or num % 10 != 0