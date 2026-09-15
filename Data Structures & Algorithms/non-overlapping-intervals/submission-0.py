class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Your code goes here
        if not intervals: 
            return 0
            
        intervals.sort(key=lambda x: x[1])

        current_end = intervals[0][1]
        to_remove = 0

        for i in range(1, len(intervals)):
            if intervals[i][0] < current_end:
                to_remove += 1
            else:
                current_end = intervals[i][1]
        
        return to_remove