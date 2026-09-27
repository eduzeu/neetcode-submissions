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

        def bactrack(i, currStr):

            if  len(currStr)== len(digits):
                res.append(currStr)
                return 
            
            for digit in phoneDigits[digits[i]]:
                bactrack(i + 1, currStr + digit)
            
        if digits:
            bactrack(0, "")

        return res
