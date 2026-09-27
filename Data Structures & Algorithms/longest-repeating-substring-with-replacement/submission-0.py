class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        #count frequency 
        chars = {} 
        maxFreq = float('-inf')
        l = 0
        replacements = 0
        #iterate trough array 
        for r in range(len(s)):
            chars[s[r]] = chars.get(s[r], 0) + 1 
            maxFreq = max(maxFreq, chars[s[r]])
            #we want to compute maxLen - maxCount
        
            while (r -l + 1) - maxFreq > k: 
                chars[s[l]] -= 1
                l += 1

            #the result is the number of replacements
            replacements = max(replacements, r- l + 1)
            #if replacements <= k then update 
            #if not then cut window until becomes valid 
        return replacements