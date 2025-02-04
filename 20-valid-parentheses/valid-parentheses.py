class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            print(i)
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            elif len(stack) == 0:
                return False
            elif i == ')' and stack[-1] == '(':
                stack.pop()
            elif i == '}' and stack[-1] == '{':
                stack.pop()
            elif i == ']' and stack[-1] == '[':
                stack.pop()
            else:
                return False
        return len(stack) == 0