import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }

        for token in tokens:
            if token in ops:
                operand2, operand1 = stack.pop(), stack.pop()

                res = ops[token](operand1, operand2)
                stack.append(int(res))
            else:
                stack.append(int(token))
        
        return stack[0]
