class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (start_pos, height)
        max_area = 0

        for idx, height in enumerate(heights):
            curr_start_pos = idx

            while stack and height < stack[-1][1]:
                start_pos, rect_height = stack.pop()

                area = (idx - start_pos) * rect_height
                max_area = max(max_area, area)

                curr_start_pos = start_pos
            
            stack.append((curr_start_pos, height))
        
        
        while stack:
            start_pos, rect_height = stack.pop()

            area = (len(heights) - start_pos) * rect_height
            max_area = max(max_area, area)
        
        return max_area