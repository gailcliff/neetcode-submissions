class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # (index, temp)
        output = [0] * len(temperatures)

        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                index, temperature = stack.pop()

                output[index] = idx - index
            
            stack.append((idx, temp))
        
        return output