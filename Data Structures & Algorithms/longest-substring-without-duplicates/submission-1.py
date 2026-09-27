class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        chars = {} 
        longest, l = 0, 0 

        for i in range(len(s)): 

            chars[s[i]] =  chars.get(s[i], 0) + 1 #count frequency

            while chars[s[i]] > 1: 
                chars[s[l]] -= 1
                l += 1 
            
            longest = max(longest, i - l + 1 )

        return longest

