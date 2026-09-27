import math 
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

      

        l, r = 1, max(piles)
        res= 0 
        while l <= r: 

            m = (l + r) //2 

            ratio = 0
            for k in piles: 
                ratio += math.ceil(k / m)
            
            if ratio <= h:
                res = m 
                r = m - 1
            else:
                l = m + 1
        
        return res



        
        