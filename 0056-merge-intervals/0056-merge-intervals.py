"""
=========================================
Problem: 56. Merge Intervals (Medium)
=========================================

CHEAT SHEET:
* Trigger: "Merge overlapping intervals", "return non-overlapping intervals".
* Trap: Trying to compare intervals without sorting them first. This leads to a messy O(N^2) brute force solution.
* Mechanism: 
    1. Sort the intervals by start time.
    2. Create an empty `merged` array.
    3. Loop through the intervals. 
    4. If `merged` is empty, or the current interval's start is > the last merged interval's end, they don't overlap. Append it.
    5. If they DO overlap, update the end time of the last merged interval to the max of both end times.

Complexity:
* Time: O(N log N) for sorting. The merge loop is O(N).
* Space: O(N) to store the output.
=========================================
"""

class Solution:
    def merge(self, intervals):
        # sort strictly by the starting time
        intervals.sort(key=lambda x: x[0])
        merged = []

        for interval in intervals:
            # if our tracker is empty or there's no overlap, just drop it in
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # overlap found, extend the end time of the last interval we tracked
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

# ---------------------------------------
# Local Testing
# ---------------------------------------
if __name__ == "__main__":
    sol = Solution()
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    
    print("Merged Intervals: {}".format(sol.merge(intervals)))