class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ''
        for s in strs: 
            encodedStr += str(len(s)) + "@" + s 
        return encodedStr
      
            
    def decode(self, s: str) -> List[str]:

        i = 0 
        ans = []

        while i < len(s):
            j = i 
            while s[j] != "@": #determine len 
                j += 1
            length = int(s[i:j])
            ans.append(s[j+1: j+1 + length])
            i = j + 1 + length 
        
        return ans



