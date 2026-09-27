class Solution:
    def longestPalindrome(self, s: str) -> str:


        def isPal(st):
            return st == st[::-1]

        longest_pal = ""
        
        for i in range(len(s)):

            l, r = i, i 
            
            #odd palindromes
            while l >= 0 and r < len(s) and isPal(s[l:r+1]): 
                if len(longest_pal) < len(s[l:r+1]):
                    longest_pal = s[l:r+1]

                l -= 1
                r += 1
            
            #even palindromes
            l, r = i, i + 1

            while l >= 0 and r < len(s) and isPal(s[l:r+1]):
                if len(longest_pal) < len(s[l:r+1]):
                    longest_pal = s[l:r+1]

                l -= 1
                r += 1
        
        return longest_pal




        

        