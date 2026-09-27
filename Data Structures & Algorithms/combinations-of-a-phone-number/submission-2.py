class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        res = []

        letters = {
            "2": "abc", 
            "3": "def", 
            "4": "ghi", 
            "5": "jkl", 
            "6": "mno", 
            "7": "pqrs", 
            "8": "tuv", 
            "9": "wxyz", 
        }

        def backtrack(curr, i): 
            if len(curr) == len(digits): 
                res.append(curr)
                return 
            
            for digit in letters[digits[i]]:
                backtrack(curr + digit, i + 1)
            
        if digits: 
            backtrack('', 0)
        return res
        