class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # variable length sliding window
        window = defaultdict(int)
        max_len = 0

        start = 0

        for end in range(len(s)):
            window[s[end]] += 1

            while window[s[end]] > 1:
                window[s[start]] -= 1
                start += 1
            
            max_len = max(max_len, end - start + 1)
        
        return max_len