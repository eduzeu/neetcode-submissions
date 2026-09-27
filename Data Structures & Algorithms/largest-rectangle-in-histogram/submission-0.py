class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        maxArea = 0
        stack = [] #pair: (index, height)

        for i, h in enumerate(heights): 
            start = i 
            while stack and stack[-1][1] > h: 
                idx, hei = stack.pop()
                w = i - idx 
                a = w * hei 
                maxArea = max(maxArea, a)
                start = idx
            stack.append((start, h))


        for i, h in stack: 
            maxArea = max(maxArea, h * (len(heights)- i))
        
        return maxArea

        