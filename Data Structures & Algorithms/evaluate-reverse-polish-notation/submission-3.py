import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }

        stack = []

        for ch in tokens:
            if ch not in operations:
                stack.append(int(ch))
            else:
                b, a = stack.pop(), stack.pop()
                res = operations[ch](a, b)
                stack.append(int(res))
        
        return stack[0]