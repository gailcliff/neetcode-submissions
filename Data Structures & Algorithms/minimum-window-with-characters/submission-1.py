from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(t) > len(s):
            return ""
        
        target = Counter(t)
        window = defaultdict(int)

        have, need = 0, len(target)
        result = (-1, -1)
        result_len = float('inf')

        start = 0
        
        for end in range(len(s)):
            ch = s[end]
            window[ch] += 1

            if ch in target and window[ch] == target[ch]:
                have += 1
            
            while have == need:
                if end - start + 1 < result_len:
                    result_len = end - start + 1
                    result = (start, end)
                
                ch = s[start]
                window[ch] -= 1

                if ch in target and window[ch] < target[ch]:
                    have -= 1
                
                start += 1

        return s[result[0]: result[1] + 1] \
            if result_len != float('inf') else ""
