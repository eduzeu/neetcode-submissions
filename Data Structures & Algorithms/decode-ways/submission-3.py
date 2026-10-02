class Solution:
    def numDecodings(self, s: str) -> int:



        dp = {} 

        def dfs(i):
          
            if i >= len(s): 
                return 1 
            if s[i] == '0':
                return 0
            if i in dp:
                return dp[i]
            

            total = dfs(i+1)

            if i + 1 < len(s) and (
    int(s[i]) == 1 or
    int(s[i]) == 2 and int(s[i:i+2]) in range(20, 27)
):
                total += dfs(i+2)
            
            dp[i] = total
            return dp[i]
        
        return dfs(0)