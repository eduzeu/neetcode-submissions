class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []

        subsets = []

        def dfs(i):

            if i >= len(nums):
                res.append(subsets.copy())
                return 
                 
            

            subsets.append(nums[i])

            #two cases: include the current and not include it
            dfs(i + 1)
            #do not inlcude the current, decide not to add to subset 
            subsets.pop()
            dfs(i+ 1)

        dfs(0)
        return res 
        