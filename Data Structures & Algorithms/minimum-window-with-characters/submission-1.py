from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        targetMap = Counter(t)
        subchars = {}
        substring = ""
        j= 0
        required = len(targetMap)
        formed = 0
        
        for i in range(len(s)):

            if s[i] in targetMap: 
                subchars[s[i]] = subchars.get(s[i], 0) + 1 #occurences of t chars
                if subchars[s[i]] == targetMap[s[i]]:
                    formed += 1
            
            #check if valid susbstring
            while formed == required:
                #case when string is empty: 
                if not substring or len(substring) > (i - j + 1):
                    substring = s[j:i+1]
                
                #check if letter to delete is in t
                if s[j] in subchars: 
                    subchars[s[j]] -= 1
                    if subchars[s[j]] < targetMap[s[j]]: 
                        formed -=1
                    if subchars[s[j]] == 0:
                        del subchars[s[j]] 
                j += 1

        return substring