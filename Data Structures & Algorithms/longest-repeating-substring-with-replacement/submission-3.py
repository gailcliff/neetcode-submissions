class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        start = 0
        ch_freqs = defaultdict(int)
        max_ch_freq = 0
        longest_substr = 0

        for end in range(len(s)):
            ch_freqs[s[end]] += 1
            max_ch_freq = max(max_ch_freq, ch_freqs[s[end]])

            while (end - start + 1) - max_ch_freq > k:
                ch_freqs[s[start]] -= 1
                start += 1
            
            longest_substr = max(longest_substr, end - start + 1)
        
        return longest_substr
