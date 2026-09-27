class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        # [[1,3],[4,6]]
        # [[1,3],[2,5],[4,6]]

 
        #find right position using binary search 

        low = 0 
        high = len(intervals) -1 
        
        while low <= high: 
            mid = low + (high - low) //2

            #move right 
            if intervals[mid][0] < newInterval[0]:
                low = mid + 1
            #move left 
            else:
                high = mid - 1
        
        intervals.insert(low, newInterval )
        
        #MERGE overlapping intervals
        merged = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = merged[-1][1]

            if lastEnd >= start: 
                merged[-1][1] = max(lastEnd, end)
            else:
                merged.append([start,end])
        
        return merged

        
