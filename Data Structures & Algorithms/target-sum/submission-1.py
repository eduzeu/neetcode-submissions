class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        

        def dfs(i, total):
            if i == len(nums):
                return total == target
            
            add = dfs(i+1, total + nums[i])
            subtract = dfs(i+1, total - nums[i])

            return add + subtract
        
        return dfs(0,0)
        