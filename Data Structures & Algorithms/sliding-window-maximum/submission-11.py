class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # [1 2 3 4 5 6]

        queue = deque()
        result = []
        start = 0

        for end in range(len(nums)):
            while queue and nums[end] > nums[queue[-1]]:
                queue.pop()
            
            queue.append(end)

            if end - start + 1 == k:
                result.append(nums[queue[0]])

                start += 1

                if start > queue[0]:
                    queue.popleft()

        return result