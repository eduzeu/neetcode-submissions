class Solution:
    def maxArea(self, heights: List[int]) -> int:

        maxArea = 0 
        l, r = 0, len(heights) -1 

        
        while l < r: 
            width = r - l 
            height = min(heights[l], heights[r])
            curr_area =  height * width

            if heights[l] <= heights[r]: 
                l += 1
            else: 
                r -= 1 

            maxArea = max(maxArea, curr_area)
        return maxArea        