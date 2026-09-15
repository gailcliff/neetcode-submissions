class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)

        if m > n: return False

        target_vector = [0] * 26
        window_vector = [0] * 26

        for i in range(m):
            target_vector[ord(s1[i]) - ord('a')] += 1
            window_vector[ord(s2[i]) - ord('a')] += 1
        
        for j in range(m, n):
            if window_vector == target_vector:
                return True
            
            window_vector[ord(s2[j - m]) - ord('a')] -= 1
            window_vector[ord(s2[j]) - ord('a')] += 1
        
        return window_vector == target_vector