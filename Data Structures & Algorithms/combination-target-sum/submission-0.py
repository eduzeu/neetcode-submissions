class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []

        def dfs(i, curr, total):
            #if total equals target then we found a valid combination 
            if total == target:    
                res.append(curr.copy())
                return 
            #if we are out of bounds or the total exceeds the target then we don't keep going 
            if i >= len(nums) or total > target: 
                return 
            
            curr.append(nums[i])
            #there are two cases: 
                #when we are including the number for n times 
                #when we are not including the number to avoid repetitions 
            
            #including number: 
            dfs(i, curr, total + nums[i])

            #excluding number: 
            curr.pop()

            dfs(i+1, curr, total )
        
        dfs(0, [], 0)
        return res


