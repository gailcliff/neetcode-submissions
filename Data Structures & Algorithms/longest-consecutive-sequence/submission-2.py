class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        memo = {}

        def dp(num):
            if num not in num_set:
                return 0

            if num in memo:
                return memo[num]

            memo[num] = 1 + dp(num + 1)
            return memo[num]

        longest = 0

        for num in num_set:
            longest = max(longest, dp(num))

        return longest