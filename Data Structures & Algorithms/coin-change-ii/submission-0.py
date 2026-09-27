class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        cache = {}

        def dfs(i, currSum): 
            
            if currSum == amount: 
                return 1 

            #base case: out of bounds
            if currSum > amount or i >= len(coins):
                return 0 
            
            if (i, currSum) in cache: 
                return cache[(i, currSum)]

            
            #include the number
            take = dfs(i, currSum + coins[i])

            #exclude and move
            skip = dfs(i+1, currSum)

            cache[(i, currSum)] = take + skip

            return cache[(i, currSum)]
        return dfs(0, 0)
        