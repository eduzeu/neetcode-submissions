class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        res = 0 
        def pows(x, n): 
            if x == 0: 
                return 0 
            if n == 0: 
                return 1 
        
            half = pows(x, n//2)

            if n % 2 == 0: 
                return half * half
            else:
                return half * half * x
            
        return pows(x,n) if n >= 0 else 1/pow(x,-n)