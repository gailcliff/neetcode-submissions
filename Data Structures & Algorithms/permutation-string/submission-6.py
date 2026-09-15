class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)

        if m > n:
            return False


        target_vector = [0] * 26
        window_vector = [0] * 26

        for i in range(m):
            target_vector[ord(s1[i]) - ord('a')] += 1
            window_vector[ord(s2[i]) - ord('a')] += 1

        for i in range(m, n):
            if target_vector == window_vector:
                return True

            window_vector[ord(s2[i]) - ord('a')] += 1
            window_vector[ord(s2[i - m]) - ord('a')] -= 1

        return target_vector == window_vector

if __name__ == '__main__':
    solution = Solution()
    print(solution.checkInclusion('abc', 'lecabee'))