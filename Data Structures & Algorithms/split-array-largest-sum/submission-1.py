class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left, right = max(nums), sum(nums)

        while left <= right:
            mid = (left + right) // 2

            num_subarrays = 1
            subarray_sum = 0

            for num in nums:
                if subarray_sum + num > mid:
                    num_subarrays += 1
                    subarray_sum = num
                else:
                    subarray_sum += num
            
            if num_subarrays <= k:
                right = mid - 1
            else:
                left = mid + 1
        
        return left