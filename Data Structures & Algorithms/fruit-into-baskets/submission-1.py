from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start = 0
        window = defaultdict(int)
        max_fruits = 0

        for end in range(len(fruits)):
            window[fruits[end]] += 1

            while len(window) > 2:
                window[fruits[start]] -= 1
                if window[fruits[start]] == 0:
                    del window[fruits[start]]

                start += 1
            
            max_fruits = max(max_fruits, end - start + 1)
        
        return max_fruits