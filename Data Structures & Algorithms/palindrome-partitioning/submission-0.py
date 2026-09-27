class Solution:
    def partition(self, s: str) -> List[List[str]]:


        res = []
        part = []

        def dfs(i): 
            #base case 
            if i >= len(s):
                res.append(part.copy())
                return 
            
            #at each index, explore the substrings
            for j in range(i, len(s)):
                if self.isPalindrome(s[i:j+1]): #check current substring 
                    part.append(s[i:j+1])
                    dfs(j+ 1)
                    part.pop()  #backtrack 
            
        dfs(0)

        return res 



    def isPalindrome(self, st):
        return True if st == st[::-1] else False 
    