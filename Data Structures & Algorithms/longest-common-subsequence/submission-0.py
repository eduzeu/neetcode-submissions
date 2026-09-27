class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        dp = []
        
        for row in range(len(text1) + 1):
            dp.append([])
            for col in range(len(text2)+ 1):
                dp[row].append(0)
        
        for i in range(len(text1)-1,-1,-1):
            for j in range(len(text2)-1,-1,-1):
                #two cases: when the character is equal and when is not

                #if the characters match:
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else: 
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        
        return dp[0][0]

        