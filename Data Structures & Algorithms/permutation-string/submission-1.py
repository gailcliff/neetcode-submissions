class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)

        if m > n:
            return False

        need = [0] * 26
        window = [0] * 26

        for i in range(m):
            need[ord(s1[i]) - ord('a')] += 1
            window[ord(s2[i]) - ord('a')] += 1

        if window == need:
            return True

        for right in range(m, n):
            # Include the new character on the right.
            window[ord(s2[right]) - ord('a')] += 1

            # Remove the character that falls out on the left.
            left = right - m
            window[ord(s2[left]) - ord('a')] -= 1

            if window == need:
                return True

        return False