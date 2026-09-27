class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:


        combinations = []

        def backtrack(i, curr_comb, curr_sum): 
            if curr_sum == target:
                combinations.append(curr_comb.copy())
                return 
            if i >= len(nums) or curr_sum > target: 
                return 
            
            curr_comb.append(nums[i])
            backtrack(i, curr_comb, curr_sum + nums[i])

            curr_comb.pop() 
            backtrack(i+1, curr_comb, curr_sum)

        backtrack(0, [], 0)
        return combinations
        