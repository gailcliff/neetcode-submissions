class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        anagram = defaultdict(int)

        for i in range(len(s)):
            anagram[s[i]] += 1
            anagram[t[i]] -= 1
        
        for val in anagram.values():
            if val != 0:
                return False
        
        return True
