# class KthLargest:

#     def __init__(self, k: int, nums: List[int]):
#         self.minHeap, self.k = nums, k
#         heapq.heapify(self.minHeap)
#         while len(self.minHeap) > k:
#             heapq.heappop(self.minHeap)

#     def add(self, val: int) -> int:
#         heapq.heappush(self.minHeap, val)
#         if len(self.minHeap) > self.k:
#             heapq.heappop(self.minHeap)
#         return self.minHeap[0]
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
            if val > self.heap[0]:
                heapq.heappushpop(self.heap, val)
        
        return self.heap[0]
