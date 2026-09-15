class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # (idx, temp)
        result = [0] * len(temperatures)

        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                stack_idx, stack_temp = stack.pop()

                result[stack_idx] = idx - stack_idx
            
            stack.append((idx, temp))
        
        return result