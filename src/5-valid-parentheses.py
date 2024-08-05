# Complexity (n = length of input string)  
class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # stack to keep track of open brackets
        close_open = {")": "(", "}": "{", "]": "["} # map close brackets to open brackets
        for el in s:
            if el in close_open: 
                if stack and stack[-1] == close_open[el]: # check if the last open bracket is the corresponding one
                    stack.pop() # remove the open bracket
                else:
                    return False # if the last open bracket is not the corresponding one, the string is invalid
            else: 
                stack.append(el) # add open brackets to the stack
                
        return True if not stack else False