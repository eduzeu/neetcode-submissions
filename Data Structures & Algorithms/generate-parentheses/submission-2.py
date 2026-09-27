class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ans = []
        
        def backtrack(op, clos, valid):
            if op == n and clos == n:
                ans.append(valid)
                return
            
            if op < n:
                backtrack(op + 1, clos ,valid + "(")
            
            if clos < op:
                backtrack(op, clos + 1, valid + ")")
            
        
        backtrack(0,0, "")
        return ans