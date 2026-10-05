class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        target_vector = [0] * 26
        window_vector = [0] * 26

        i = 0
        while i < len(s1):
            target_vector[ord(s1[i]) - ord('a')] += 1
            window_vector[ord(s2[i]) - ord('a')] += 1
            i += 1

        start = 0
        for end in range(i, len(s2)):
            if target_vector == window_vector:
                return True
            
            window_vector[ord(s2[end]) - ord('a')] += 1
            window_vector[ord(s2[start]) - ord('a')] -= 1
            start += 1
        
        return target_vector == window_vector