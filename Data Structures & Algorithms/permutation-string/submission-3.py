class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        m, n = len(s1), len(s2)
        
        target_vector = [0] * 26
        window_vector = [0] * 26

        for i in range(m):
            target_vector[ord(s1[i]) - ord('a')] += 1
            window_vector[ord(s2[i]) - ord('a')] += 1

        # if window_vector == target_vector:
                # return True
        
        for end in range(m, n):
            if window_vector == target_vector:
                return True

            start = end - m # i.e , end - window length
            # m is the length of s1, which is the length of our
            # window

            window_vector[ord(s2[end]) - ord('a')] += 1
            window_vector[ord(s2[start]) - ord('a')] -= 1
        
        return window_vector == target_vector


        
