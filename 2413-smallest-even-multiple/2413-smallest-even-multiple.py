class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        # If n is even, it is already the smallest multiple of both 2 and n
        # If n is odd, the smallest common multiple is 2 * n
        return n if n % 2 == 0 else 2 * n
