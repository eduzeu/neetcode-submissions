class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        i = 0
        stack = []
        num = 0
        sign = "+"

        while i < len(s):
            if s[i].isdigit():
                num = num * 10 + int(s[i])

            if not s[i].isdigit() or i == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                elif sign == "/":
                    stack.append(int(stack.pop() / num))  # Truncate toward zero

                sign = s[i]
                num = 0
            i += 1

        return sum(stack)
