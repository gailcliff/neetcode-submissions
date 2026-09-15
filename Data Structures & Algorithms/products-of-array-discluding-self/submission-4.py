class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix_products = []
        suffix_products = [0] * len(nums)

        prefix = 1
        suffix = 1

        for i in range(len(nums)):
            prefix_products.append(prefix)
            prefix *= nums[i]
        
        print(prefix_products)
        
        for i in range(len(nums) - 1, -1, -1):
            suffix_products[i] = suffix
            suffix *= nums[i]
        
        print(suffix_products)
        
        return [prefix_products[i] * suffix_products[i] for i in range(len(nums))]