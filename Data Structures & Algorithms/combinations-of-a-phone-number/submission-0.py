class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phoneDigits = {
            '2': "abc",
            "3": "def",
            "4": "hgi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []

        def backtrack(i, currStr):
            #base case: we have reached the length of the string 
            if len(currStr) == len(digits):
                res.append(currStr)
                return #backtrack 
            for d in phoneDigits[digits[i]]:
                backtrack(i+ 1, currStr + d)
            
        if digits: 
            backtrack(0, '')
        
        return res
                
