class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_l, max_r = height[l], height[r]
        total_water = 0

        while l < r:
            if max_l < max_r:
                l += 1

                if max_l > height[l]:
                    water_here = max_l - height[l]
                    total_water += water_here
                else:
                    max_l = height[l]
            else:
                r -= 1

                if max_r > height[r]:
                    water_here = max_r - height[r]
                    total_water += water_here
                else:
                    max_r = height[r]
        
        return total_water
