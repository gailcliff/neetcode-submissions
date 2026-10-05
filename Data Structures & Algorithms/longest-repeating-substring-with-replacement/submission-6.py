class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        start = 0
        mode_char_count = 0
        window = defaultdict(int)
        max_len = 0

        for end in range(len(s)):
            window[s[end]] += 1
            mode_char_count = max(mode_char_count, window[s[end]])

            while (end - start + 1) - mode_char_count > k:
                window[s[start]] -= 1
                start += 1
            
            max_len = max(max_len, end - start + 1)
        
        return max_len