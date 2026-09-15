class Solution:
    def trap(self, height: List[int]) -> int:
        # calculate water trapped on top of each bar

        l, r = 0, len(height) - 1

        left_max, right_max = height[l], height[r]
        total_water = 0

        while l < r:
            if left_max < right_max:
                l += 1

                if height[l] < left_max:
                    water_here = left_max - height[l]
                    total_water += water_here
                else:
                    left_max = height[l]
            else:
                r -= 1

                if height[r] < right_max:
                    water_here = right_max - height[r]
                    total_water += water_here
                else:
                    right_max = height[r]
        
        return total_water