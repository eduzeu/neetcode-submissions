class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        total = 0
        res = []
        
        for i in range(len(nums) - k +1):
            window = nums[i:i+k]
            res.append(max(window))
        
        return res

        