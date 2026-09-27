class Solution:
    def numDecodings(self, s: str) -> int:

        ways = {}


        def decode(i):

            if i >= len(s):
                return 1

            if s[i] == '0':
                return 0
            
            if i in ways: 
                return ways[i]
            

        
            totalWays = decode(i+1)

            #check if second is possible

            if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                totalWays += decode(i+2)
            
            ways[i] = totalWays
        
            return totalWays
        
        return decode(0)
        