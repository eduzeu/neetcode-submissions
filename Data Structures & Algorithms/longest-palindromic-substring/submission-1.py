class Solution:
    def longestPalindrome(self, s: str) -> str:

        res = ''
        strLen = 0

        for i in range(len(s)):

            #case 1: length of the input is odd

            l, r = i, i 
            while l >= 0 and r <= len(s) -1 and s[l] == s[r]: 
                if (r - l + 1) > strLen: 
                    res = s[l:r+1] #update string
                    strLen = r - l + 1
                l -= 1
                r +=1
            
            #case 2: odd len

            l, r = i, i + 1
            while l >= 0 and r <= len(s) -1 and s[l] == s[r]: 
                if (r - l + 1) > strLen: 
                    res = s[l:r+1] #update string
                    strLen = r - l + 1
                l -= 1
                r +=1
        
        return res

        