class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        start = 0
        window = defaultdict(int)
        highest_char_count = 0
        longest_substr_len = 0

        for end in range(len(s)):
            window[s[end]] += 1
            highest_char_count = max(highest_char_count, 
                                    window[s[end]])
            
            while (end - start + 1) - highest_char_count > k:
                window[s[start]] -= 1
                start += 1
            
            longest_substr_len = max(longest_substr_len, 
                                    end - start + 1)
        
        return longest_substr_len
