class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        max_seq_len = 0

        for num in nums:
            if (num - 1) not in unique:
                # means we can start new seq here
                seq_len = 1
                while (num + seq_len) in unique:
                    seq_len += 1
                
                max_seq_len = max(max_seq_len, seq_len)
        
        return max_seq_len