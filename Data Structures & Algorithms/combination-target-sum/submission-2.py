class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []


        def backtrack(i, currSum, sumarr):

            if i >= len(nums) or currSum > target: 
                return 

            if currSum == target: 
                res.append(sumarr.copy())
                return 
            
            #inlcude number
            sumarr.append(nums[i])
            backtrack(i, currSum + nums[i], sumarr )

            sumarr.pop()
            backtrack(i +1, currSum, sumarr)

        
        backtrack(0, 0, [])
        return res
            
        

