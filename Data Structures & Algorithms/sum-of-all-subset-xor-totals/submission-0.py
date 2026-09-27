class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        subsets = []

        def dfs(i, sub):
            if i >= len(nums):
                subsets.append(sub.copy())
                return 
        
            #include number
            sub.append(nums[i])
            dfs(i+1, sub)

            #exclude number
            sub.pop()
            dfs(i+1, sub)
            
        xors = []
        dfs(0, [])

        for sub in subsets: 
            total = 0
            
            for n in sub:
                total = total ^ n
            xors.append(total)
            
        return sum(xors)




        