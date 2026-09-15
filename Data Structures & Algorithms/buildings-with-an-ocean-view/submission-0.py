class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = []

        for i, height in enumerate(heights):
            while stack and height >= heights[stack[-1]]:
                stack.pop()
            stack.append(i)
        
        return stack
