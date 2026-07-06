"""
=========================================
Problem: 56. Merge Intervals (Medium)
=========================================

CHEAT SHEET:
* Trigger: "Merge overlapping intervals", "return non-overlapping intervals".
* Trap: Trying to compare intervals without sorting them first. This leads to an O(N^2) brute force disaster where you have to constantly look forwards and backwards.
* Mechanism: 
    1. Sort the intervals based strictly on their start times using `intervals.sort(key=lambda x: x[0])`.
    2. Create an empty `merged` list.
    3. Iterate through the intervals. 
    4. If `merged` is empty, or the current interval's start is strictly greater than the last merged interval's end (`merged[-1][1] < interval[0]`), they don't overlap. Append it.
    5. If they DO overlap, update the end time of the last merged interval to the `max` of both end times.

Complexity:
* Time: O(N log N) dominated strictly by the sorting step. The actual merging loop is O(N).
* Space: O(N) to store the output array of merged intervals.
=========================================
"""

class Solution:
    def merge(self, intervals):
        # Step 1: Sort intervals by their start time
        intervals.sort(key=lambda x: x[0])

        merged = []

        # Step 2: Traverse and merge
        for interval in intervals:
            # If the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Otherwise, there is overlap, so we merge the current and previous interval.
                merged[-1][1] = max(merged[-1][1], interval[1])
                    
        # Step 3: Return AFTER the loop is completely finished
        return merged

# ---------------------------------------
# Driver Code for Local / GitHub Testing
# ---------------------------------------
if __name__ == "__main__":
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    
    # Using classic .format() for universal Python compatibility
    print("Original Intervals: {}".format(intervals))
    
    obj = Solution()
    result = obj.merge(intervals)
    
    print("Merged Intervals:   {}".format(result))