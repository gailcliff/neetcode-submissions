class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = [] # list of (idx, height)
        max_area = 0
        n = len(heights)

        for i, height in enumerate(heights):
            start = i
            while stack and height < stack[-1][1]:
                idx, ended_height = stack.pop()
                ended_area = ended_height * (i - idx)
                max_area = max(max_area, ended_area)
                start = idx
            
            stack.append((start, height))
        
        while stack:
            idx, survived_height = stack.pop()
            max_area = max(max_area, survived_height * (n - idx))
        
        return max_area
        