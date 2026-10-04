class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_unique = set(nums)
        max_seq_len = 0

        for num in nums_unique:
            # can this integer start a sequence
            if (num - 1) not in nums_unique:
                seq_len = 1
                while num + seq_len in nums_unique:
                    seq_len += 1
                
                max_seq_len = max(max_seq_len, seq_len)
        
        return max_seq_len