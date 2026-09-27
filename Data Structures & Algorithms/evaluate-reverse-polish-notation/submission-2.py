class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        total = 0

        for i in range(len(tokens)):
            if tokens[i] == "+":
                operand1 = stack.pop()
                operand2 = stack.pop()
                stack.append(operand1 + operand2)
            elif tokens[i] == "-":
                operand1 = stack.pop()
                operand2 = stack.pop()
                stack.append(operand2 - operand1)

            elif tokens[i] == "*":
                operand1 = stack.pop()
                operand2 = stack.pop()
                stack.append(operand1 * operand2)
            elif tokens[i] == "/":
                operand1 = stack.pop()
                operand2 = stack.pop()
                stack.append(int(operand2 / operand1))
            else: 
                stack.append(int(tokens[i]))
        
        ans = stack.pop()
        return ans

         