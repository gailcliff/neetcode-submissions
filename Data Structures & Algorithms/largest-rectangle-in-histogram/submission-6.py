class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (pos, height)
        max_area = 0

        for idx, height in enumerate(heights):
            start_idx = idx

            while stack and height < stack[-1][1]:
                rect_start, rect_height = stack.pop()

                area = (idx - rect_start) * rect_height
                max_area = max(max_area, area)

                start_idx = rect_start
            
            stack.append((start_idx, height))
        
        while stack:
            start_idx, height = stack.pop()
            area = (len(heights) - start_idx) * height
            max_area = max(max_area, area)
        

        return max_area