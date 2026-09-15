class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        memo = dict.fromkeys(nums, 1)
        max_seq = 0

        for n in nums:
            if n-1 in memo:
                memo[n] = memo[n-1] + 1
            
            max_seq = max(max_seq, memo[n])
        
        return max_seq