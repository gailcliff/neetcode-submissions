class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_products, suffix_products = {0: 1}, {len(nums)-1: 1}

        i = 1
        while i < len(nums):
            prefix_products[i] = nums[i-1] * prefix_products[i-1]
            i += 1

        i = len(nums) - 2
        while i >= 0:
            suffix_products[i] = nums[i+1] * suffix_products[i+1]
            i -= 1

        products = [v * suffix_products[k] for k, v in prefix_products.items()]
        
        return products