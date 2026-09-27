import math
class Solution:
    def numSquares(self, n: int) -> int:

        dp = {}

        def dfs(n):
            
            if n in dp:
                return dp[n]

            if n == 0:
                return 0

            total = float('inf')
            for i in range(1, int(math.isqrt(n)) + 1):

                total = min(total, 1 + dfs(n - i * i))

            dp[n] = total

            return dp[n]
        
        return dfs(n)



        