class Solution(object):
    def findDuplicate(self, nums):
        slow = nums[0]
        fast = nums[0]

        # Find the meeting point
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # Find the entrance of the cycle
        fast = nums[0]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow