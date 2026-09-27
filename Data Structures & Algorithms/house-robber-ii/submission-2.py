class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = {}
        memo1 = {}

        def dfs(i, arr, memo): 
            if i >= len(arr):
                return 0 
            if i in memo: 
                return memo[i]

            memo[i] = max(dfs(i+1, arr, memo), arr[i] + dfs(i+2, arr, memo))
        
            return memo[i]
        
        if len(nums) == 1:
            return nums[0]
        arr1 = nums[1:]
        arr2 = nums[0:-1]

        return max(dfs(0, arr1, {}), dfs(0,arr2,{}))
        

        