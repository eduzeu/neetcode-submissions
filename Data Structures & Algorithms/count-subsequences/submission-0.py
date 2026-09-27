class Solution:
    def numDistinct(self, s: str, t: str) -> int:


        cache = {}

        def backtrack(i, j):
            
            if j >= len(t):
                return 1 #found subsequence
            #not found
            if i >= len(s): 
                return 0
        
            if (i, j) in cache:
                return cache[(i,j)]

            if s[i] == t[j]:
                cache[(i,j)] = backtrack(i+1, j+1) + backtrack(i+1, j) #include both
            else: 
                cache[(i,j)] = backtrack(i+1, j) #do not include
            
            return cache[(i,j)]

        return backtrack(0,0)
