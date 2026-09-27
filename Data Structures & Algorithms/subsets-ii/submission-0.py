class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
 
        nums.sort() 
        res = []

        def dfs(i, subset):
            if i >= len(nums): 
                res.append(subset.copy())
                return 
            
            subset.append(nums[i])
            #decide to stay with the number 
            dfs(i+1, subset)
            
            #decide to skip the number
            subset.pop()
            #get to the right index 
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            
            dfs(i+1, subset)
        
        dfs(0, [])

        return res


        
        