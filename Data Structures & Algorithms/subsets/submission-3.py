class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        subsets = []

        def dfs(i, currsubset): 
            if i >= len(nums):
                subsets.append(currsubset.copy())
                return 
            
            currsubset.append(nums[i])

            dfs(i+1, currsubset)

            currsubset.pop()

            dfs(i+1, currsubset)

        dfs(0, [])
        return subsets

        

      
         
        