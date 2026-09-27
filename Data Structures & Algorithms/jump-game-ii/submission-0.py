class Solution:
    def jump(self, nums: List[int]) -> int:

        far = float("-inf")
        currRange = 0 
        jumps = 0

        for i in range(len(nums)):
            far = max(far, i + nums[i])

            if i == currRange: 
                if currRange < len(nums)  -1: 
                    jumps += 1
                    currRange = far

        return jumps       