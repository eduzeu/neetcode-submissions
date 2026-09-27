class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l = 0
        r = len(heights) - 1
        maxArea = float('-inf')

        #we know area = w * h 
        #we want to take the minimum height and multiply times the distance
        ##this is because we don't want the container to slant. 

        while l < r: 

            area = (r - l) * min(heights[r], heights[l])

            if heights[l] < heights[r]:
                l += 1
            else: 
                r -= 1

            maxArea  = max(maxArea, area)

        return maxArea 




                


        