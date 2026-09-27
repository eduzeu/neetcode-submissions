class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:




        l, r = max(weights), sum(weights)
        res =0 

        def isPossible(capacity):
            days_used = 1
            currload = 0 

            for w in weights:
                if currload + w <= capacity: 
                    currload += w
                else: 
                    days_used += 1
                    currload = w

                    if days_used > days: 
                        return False
            return True 

        while l <= r: 

            cap = (l + r) // 2

            if isPossible(cap):
                res = cap 
                r = cap - 1
            else: 
                l = cap + 1
        return res


        