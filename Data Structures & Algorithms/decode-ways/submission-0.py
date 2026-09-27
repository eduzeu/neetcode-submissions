class Solution:
    def numDecodings(self, s: str) -> int:
        
        memo = {}
        def dfs(i):
        #if at last index: return total 
            if i == len(s):
                return 1 

            if s[i] == '0':
                return 0
            
            if i in memo:
                return memo[i]
            
            result = dfs(i+1)
        #if current index added to the previous is less than 26: 
            if i+ 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                result += dfs(i+2)

            memo[i] = result
            return result
        return dfs(0)
        