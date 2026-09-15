from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        queue = deque()
        result = []

        start = 0
        for end in range(len(nums)):
            while queue and nums[queue[-1]] < nums[end]:
                queue.pop()

            queue.append(end)
            # print([nums[i] for i in queue])

            if end - start + 1 == k:
                result.append(nums[queue[0]])
                start += 1

                if start > queue[0]:
                    queue.popleft()
        
        return result

