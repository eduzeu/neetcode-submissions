from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        # Binary search to find insertion position
        low, high = 0, len(intervals) - 1

        while low <= high:
            mid = low + (high - low) // 2
            if intervals[mid][0] < newInterval[0]:
                low = mid + 1
            else:
                high = mid - 1

        # Insert newInterval at the correct position
        intervals.insert(low, newInterval)

        # Merge overlapping intervals
        merged = [intervals[0]]
        for start, end in intervals[1:]:
            lastEnd = merged[-1][1]
            if lastEnd >= start:
                merged[-1][1] = max(lastEnd, end)  # Merge intervals
            else:
                merged.append([start, end])

        return merged
