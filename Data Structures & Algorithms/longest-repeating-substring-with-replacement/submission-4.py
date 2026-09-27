class Solution:
    def characterReplacement(self, s: str, k: int) -> int:


        freqs = {}
        l = 0 
        longest= 0 
        maxFreq = 0


        for r in range(len(s)): 

            freqs[s[r]] = freqs.get(s[r], 0 ) + 1
            maxFreq = max(maxFreq, freqs[s[r]])

            if (r - l + 1) - maxFreq > k: 
                freqs[s[l]] -= 1
                l += 1 
            
            longest = max(longest, r - l + 1)
        
        return longest





        