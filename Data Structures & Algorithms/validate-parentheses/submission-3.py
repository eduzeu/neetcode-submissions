class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for i in range(len(s)):

            #if s[i] is opening parentheses
                #add OP to the stack 
            if s[i] == "("  or s[i] == '[' or s[i] == '{':
                stack.append(s[i])

            elif s[i] == ')':
                if not stack or stack.pop() != '(':
                    return False
               
            
            elif s[i] == ']':
                if not stack or stack.pop() != '[':
                    return False
          
            
            elif s[i] == '}':
                if not stack or stack.pop() != '{':
                    return False
        
        return len(stack) == 0

            #if s[i] is closing parentheses 
                #compare with OP type at top of stack 
                #if CP and OP are of the same type
                    #pop from our stack and continue iterating
                #ELSE we return false 
         