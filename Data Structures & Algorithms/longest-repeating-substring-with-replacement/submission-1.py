class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = 0 
        chars = {}
        maxLen = float('-inf')
        l = 0 

        for r in range(len(s)): 
            c = s[r]
            chars[c] = chars.get(c, 0) + 1
            maxLen = max(maxLen, chars[c])

            while (r - l + 1) - maxLen > k: 
                chars[s[l]] -=1
                l += 1
            
            count = max(count, r - l + 1)

        return count