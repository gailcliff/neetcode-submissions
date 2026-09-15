class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        products = [1] * len(nums)

        prefix_product = 1
        for i in range(len(nums)):
            products[i] = prefix_product
            prefix_product *= nums[i]
        
        postfix_product = 1
        for i in range(len(nums) - 1, -1, -1):
            products[i] *= postfix_product
            postfix_product *= nums[i]
        
        return products