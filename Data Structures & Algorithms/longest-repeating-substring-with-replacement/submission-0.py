class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # extend the string

        start = 0
        char_freqs = defaultdict(int)
        max_char_freq = 0
        longest_substr = 0

        for end in range(len(s)):
            char_freqs[s[end]] += 1
            
            max_char_freq = max(max_char_freq, char_freqs[s[end]])

            while (end - start + 1) - max_char_freq > k:
                char_freqs[s[start]] -= 1

                start += 1
            
            longest_substr = max(longest_substr, end - start + 1)
        
        return longest_substr
