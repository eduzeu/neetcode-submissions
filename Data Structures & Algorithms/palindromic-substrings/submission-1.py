class Solution:
    def countSubstrings(self, s: str) -> int:

        
        substrings = 0 

        def isPal(st):
            return st == st[::-1]

        for i in range(len(s)):

            l, r = i, i 

            while l >= 0 and r < len(s) and isPal(s[l:r+1]):
                substrings += 1
            
                l -= 1
                r += 1
            
            l, r = i, i + 1

            while l >= 0 and r < len(s) and isPal(s[l:r+1]):
                substrings += 1

                l -=1
                r += 1
        
        return substrings 