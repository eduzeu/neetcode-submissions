class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l = 0 
        r = len(heights) -1

        maxArea = float('-inf')
        

        while l <= r: 

            height = min(heights[l], heights[r]) 
            width = r - l 
            currArea = height * width 

            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else: 
                l += 1
            
            maxArea = max(maxArea, currArea)
        
        return maxArea




        




                


        