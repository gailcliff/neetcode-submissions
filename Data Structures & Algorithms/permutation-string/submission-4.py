class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)

        if m > n:
            # in this case, s2 can't contain a permutation of s2
            # because it is shorter in length than s1 and thus
            # will contain a less number of characters
            return False
        
        target_vector = [0] * 26
        window_vector = [0] * 26

        for i in range(m):
            target_vector[ord(s1[i]) - ord('a')] += 1
            window_vector[ord(s2[i]) - ord('a')] += 1
        
        for end in range(m, n):
            if target_vector == window_vector:
                # if the counts of each character in the window
                # match those of the target, it means that
                # that window is an anagram of the target and we
                # return True
                return True

            # end is the current position of where the window ends
            # in s2.
            # start is the position of where the window starts in s2.
            # the length of the window is m, which is the entire
            # length of s2
            start = end - m

            window_vector[ord(s2[end]) - ord('a')] += 1
            window_vector[ord(s2[start]) - ord('a')] -= 1

        return window_vector == target_vector