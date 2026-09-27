class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:


        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]
        #[[1,2],[1,4],[2,4]]
        print(intervals, prevEnd)
        for start, end in intervals[1:]:

            if prevEnd <= start: 
                prevEnd = end
            else: 
                res += 1
                prevEnd = min(end, prevEnd)

        return res
