class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:


        combinations = [] 

        def dfs(i, curr_comb, curr_sum): 
            if curr_sum == target: 
                combinations.append(curr_comb[:])
                return 
            if i >= len(nums) or curr_sum > target:
                return 
            
            curr_sum += nums[i]
            curr_comb.append(nums[i])
            dfs(i, curr_comb, curr_sum)

            #not include 
            curr_sum -= nums[i]
            curr_comb.pop() 
            dfs(i+1, curr_comb, curr_sum)

    
        dfs(0, [], 0)
        return combinations 

        