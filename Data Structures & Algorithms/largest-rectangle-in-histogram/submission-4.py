class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (idx, h)
        max_area = 0
        n = len(heights)

        for i, height in enumerate(heights):
            start = i
            while stack and height < stack[-1][1]:
                # heights[stack[-1]] has been ended
                idx, h = stack.pop()
                max_area = max(max_area, h * (i - idx))
                start = idx
            stack.append((start, height))
        
        while stack:
            i, h = stack.pop()
            max_area = max(max_area, h * (n-i))
        
        return max_area