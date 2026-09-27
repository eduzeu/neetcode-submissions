class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = {} 
        #count frequency

        distance = 0 
        l = 0

        for r in range(len(s)):
            seen[s[r]] = seen.get(s[r], 0) + 1 


            while seen[s[r]] > 1:
                seen[s[l]]-= 1
                l += 1

            distance = max(distance, r - l + 1)

        return distance 

        