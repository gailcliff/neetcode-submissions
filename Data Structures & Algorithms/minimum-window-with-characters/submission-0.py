class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(t) > len(s):
            return ""
        
        target = Counter(t)
        window = defaultdict(int)
        
        have, need = 0, len(target)
        start = 0

        res = (-1, -1)
        res_len = float('inf')

        for end in range(len(s)):
            ch = s[end]
            window[ch] += 1

            if ch in target and window[ch] == target[ch]:
                have += 1
            
            # start contracting the window from the left.
            # while contracting, we might obtain a shorter
            # substring that still contains all characters of t
            while have == need:
                if (end - start + 1) < res_len:
                    # if this condition passes, we are obviously
                    # guaranteed that we have a shorter 
                    # substring (i.e more optimal) that has 
                    # all chars of t
                    res = (start, end)
                    res_len = end - start + 1
                
                ch = s[start]
                window[ch] -= 1

                # after decrementing window[ch], check if
                # our window is no longer valid, i.e it is
                # no longer a substring that contains all
                # characters of t
                if ch in target and window[ch] < target[ch]:
                    have -= 1
                
                start += 1
        
        return s[res[0] : res[1] + 1] if res_len != float('inf') else ""