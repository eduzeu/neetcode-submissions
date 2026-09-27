class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        
        dp = {}

        def backtrack(i, currSum):

            if i >= len(nums):
                return 1 if currSum == target else 0 
            
            if (i, currSum) in dp:
                return dp[(i, currSum) ]
            
            add = backtrack(i+1, currSum + nums[i])

            subtract = backtrack(i+1, currSum - nums[i])

            dp[(i, currSum) ] = add + subtract 

            return dp[(i, currSum) ]
        
        return backtrack(0,0)
        