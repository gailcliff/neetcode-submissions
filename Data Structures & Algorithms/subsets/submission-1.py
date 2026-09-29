class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = []

        working_subset = []

        def dfs(i):
            if i >= len(nums):
                result.append(working_subset[:])
                return
            
            working_subset.append(nums[i])
            dfs(i + 1)

            working_subset.pop()
            dfs(i + 1)
        
        dfs(0)
        
        return result