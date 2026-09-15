class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # variable length sliding window

        start = 0
        max_len = 0
        window = defaultdict(int)

        for end in range(len(s)):
            window[s[end]] += 1

            while window[s[end]] > 1:
                window[s[start]] -= 1

                if window[s[start]] == 0:
                    del window[s[start]]
                
                start += 1
            
            substr_len = end - start + 1
            max_len = max(max_len, substr_len)
        
        return max_len