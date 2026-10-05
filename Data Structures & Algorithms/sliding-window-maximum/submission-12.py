class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        queue = deque()
        max_nums = []

        start = 0

        for end in range(len(nums)):

            while queue and nums[end] > nums[queue[-1]]:
                queue.pop()
            
            queue.append(end)

            if end - start + 1 == k:
                max_nums.append(nums[queue[0]])

                start += 1

                if start > queue[0]:
                    queue.popleft()
        
        return max_nums