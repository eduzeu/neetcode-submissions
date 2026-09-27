import math 
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1 
        r = max(piles)
        res = 0 
        while l <= r: 
            m = (l + r )// 2

            time = 0 
            for p in piles: 
                time += math.ceil(float(p)/ m)
            
            if time <= h: 
                res = m 
                r = m - 1 
            elif time > h: 
                l = m + 1 
                
        return res






        
        