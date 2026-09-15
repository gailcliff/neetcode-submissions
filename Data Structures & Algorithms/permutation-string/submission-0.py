from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        target_count = defaultdict(int)
        window_count = defaultdict(int)

        for ch in s1:
            target_count[ch] += 1

        start = 0

        for end in range(len(s2)):
            # Add the newest character to the window
            window_count[s2[end]] += 1

            # If the window becomes too large,
            # remove the character at the left side
            if end - start + 1 > len(s1):
                left_char = s2[start]
                window_count[left_char] -= 1

                # Delete characters whose count becomes 0
                # so dictionary equality works correctly
                if window_count[left_char] == 0:
                    del window_count[left_char]

                start += 1

            # Once the window has exactly len(s1) characters,
            # check whether it has the same character frequencies as s1
            if end - start + 1 == len(s1):
                if window_count == target_count:
                    return True

        return False