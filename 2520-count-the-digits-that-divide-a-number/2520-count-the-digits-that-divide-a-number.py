class Solution(object):
    def countDigits(self, num):
        original = num
        count = 0

        while num:
            digit = num % 10
            if original % digit == 0:
                count += 1
            num //= 10

        return count