class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        memo= {}

        def dfs(currSum):
            if currSum == target:
                return 1
            
            if currSum > target:
                return 0
            
            if currSum in memo:
                return memo[currSum]
            
            total =0 
            for num in nums: 
                total += dfs(num + currSum)
            
            memo[currSum] = total

            return memo[currSum] 
        
        return dfs(0)

        
        

        
        