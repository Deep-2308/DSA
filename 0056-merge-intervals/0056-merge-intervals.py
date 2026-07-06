class Solution:
    def merge(self , intervals):

        # Step : 1 Sort intervals by their start time
        intervals.sort(key = lambda x: x[0])

        merged = []

        # Step : 2 Traverse and merge
        for interval in intervals:

            # If the list of merged intervals is empty or if thr current interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                    #Otherwise, there is overlap, so we merged the current and previous interval.
                    merged[-1][1] = max(merged[-1][1], interval[1])
                    
        return merged

