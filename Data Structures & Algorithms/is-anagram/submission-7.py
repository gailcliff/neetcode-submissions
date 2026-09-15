class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        char_counts = defaultdict(int)
        
        for i in range(len(s)):
            char_counts[s[i]] += 1
            char_counts[t[i]] -= 1
        
        for count in char_counts.values():
            if count != 0:
                return False
        
        return True