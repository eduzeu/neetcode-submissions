class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ans = []
        
        def backtrack(opening, closing, valid):
            
            if opening == n and closing == n: 
                ans.append(valid)
                return 
            
            if opening < n: 
                backtrack(opening + 1, closing, valid + "(")
            
            if closing < opening: 
                backtrack(opening, closing+ 1, valid + ")")
            
        
        backtrack(0,0, "")
        return ans