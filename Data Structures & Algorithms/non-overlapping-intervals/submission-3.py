class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:



        # [[1,2],[1,4], [2,4]]

        intervals.sort() 
        currStart, currEnd = intervals[0]
        intvals = 0 

        for start, end in intervals[1:]:
            if currEnd > start: #they overlap
                intvals += 1
                currEnd = min(end, currEnd)
            else: 
                currEnd = end

        return intvals
