class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k

        for i in range(len(nums)):
            if i < k:
                heapq.heappush(self.heap, nums[i])
            else:
                if nums[i] > self.heap[0]:
                    heapq.heappushpop(self.heap, nums[i])

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        else:
            if self.heap and val > self.heap[0]:
                heapq.heappushpop(self.heap, val)
        
        return self.heap[0]
