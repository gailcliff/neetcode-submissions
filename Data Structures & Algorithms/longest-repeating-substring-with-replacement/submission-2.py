class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # extend the string
        start = 0
        most_freq_char_count = 0
        char_counts = defaultdict(int)
        longest_substr_len = 0

        for end in range(len(s)):
            char_counts[s[end]] += 1

            most_freq_char_count = max(
                most_freq_char_count,
                char_counts[s[end]]
            )

            while (end - start + 1) - most_freq_char_count > k:
                char_counts[s[start]] -= 1
                start += 1

            longest_substr_len = max(
                longest_substr_len, 
                end - start + 1
            )
        
        return longest_substr_len