class Solution:
    def isValid(self, s: str) -> bool:
        opening_chars = ['{', '[', '(']
        closing_chars = ['}', ']', ')']
        brace_map = { '{' : '}', '[' : ']', '(' : ')' }
        str_length = len(s)
        if str_length % 2 != 0:
            return False
        
        stack = []

        for char in s:
            if char in opening_chars:
                stack.append(char)
                continue
            
            if len(stack) == 0:
                return False

            if char != brace_map[stack.pop()]:
                return False

        if len(stack) > 0:
            return False
        
        return True