class Solution:
    def isValid(self, s: str) -> bool:
        
        mappings = {
            '}': '{',
            ']': '[',
            ')': '('
        }

        stack = []
        for ch in s:
            if ch in mappings:
                if stack and stack[-1] == mappings[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        
        return not stack