class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        perms = []

        def backtrack(i, per):
      

            if len(per) == len(nums):
                perms.append(per.copy())
                return 
            
            for num in nums: 
                if num not in per: 
                    per.append(num)
                    backtrack(i+1, per)
                    per.pop()
        
        backtrack(0, [])
        return perms

            