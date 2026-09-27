class Solution:
    def trap(self, height: List[int]) -> int:

        #min(height[l], height[r]) - height[i]

        l, r = 0, len(height) - 1
        water = 0
        leftMax, rightMax = height[l], height[r]


        while l < r: 

            if height[l] < height[r]:
                l += 1
                leftMax = max(leftMax, height[l])
                water += (leftMax - height[l])
            else: 
                r -= 1
                rightMax = max(rightMax, height[r])
                water += ( rightMax  - height[r])   

        return water     