class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        strNum = ''

        for d in digits: 
            strNum += str(d)
        
        plusOne = int(strNum) + 1
        res = []

        for num in str(plusOne):
            res.append(int(num))


        return res
        