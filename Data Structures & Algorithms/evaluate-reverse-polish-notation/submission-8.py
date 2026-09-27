class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        total = 0
        
        def applyOperation(sym, op1, op2):
            if sym == "+":
                val = int(op1) + int(op2)
            elif sym == "-":
                val = int(op1) - int(op2)
            elif sym == '*':
                val = int(op1) * int(op2)
            else: 
                val = int(int(op1) / int(op2))

            return val

        for i in range(len(tokens)):

            if tokens[i].lstrip('-').isdigit(): 
                stack.append(int(tokens[i]))
            else:
                num1, num2 = stack.pop(), stack.pop()
                number = applyOperation(tokens[i], num2, num1)
                stack.append(number)
        
        return stack.pop()

        #[5]
        #
                


        
         