class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        num1 = num1[::-1]
        num2 = num2[::-1]
        mults_array = []
        zeroes = 0 

        for n1 in num1:
            carry = 0 
            multStr = ""
            for n2 in num2: 
                mult = (int(n2) * int(n1)) + carry
                result = mult % 10 
                carry = mult // 10
                multStr = str(result) + multStr
                
        
            if carry > 0: 
                multStr = str(carry) + multStr

            mults_array.append((multStr) + (zeroes * "0"))
            zeroes += 1

        total = sum(map(int, mults_array))
        return str(total)
        


        