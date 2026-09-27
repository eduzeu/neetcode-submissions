class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        relation = stairs(n-1) = stairs(n-2) = fib 
        if  n = 3 
        3   2   1   0
        1   1   2   3

        5   4   3   2   1   0 
        1   1   2   3   5   8 
        FIB SERIES
        '''

        one = 1
        two = 1 

        for i in range(n):
            temp = one 
            one = one + two 
            two = temp 
        
        return two 
        