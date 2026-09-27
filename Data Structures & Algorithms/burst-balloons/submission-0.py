class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        cache = {}
        nums = [1] + nums + [1]
        def dfs( left, right):

            if left > right:
                return 0 
            
            if (left, right) in cache:
                return cache[(left, right)]

            cache[(left, right)] = 0

            for i in range(left, right + 1):
                coins = nums[left -1] * nums[i] * nums[right + 1]
                coins += dfs(left, i-1) + dfs(i+1, right)
                cache[(left, right)] = max(cache[(left, right)], coins)
            
            return cache[(left, right)]


        return dfs(1, len(nums) - 2)


        
        