class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # use two-pointer approach

        l, r = 0, len(heights) - 1
        max_area = 0

        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            max_area = max(max_area, area)

            # we optimize for the taller height, since as we decrease the width
            # by shifting the left/right pointers inward, the only way to optimize
            # for max area is to optimize for taller heights. so we discard the 
            # shorter bar and look for taller ones
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_area