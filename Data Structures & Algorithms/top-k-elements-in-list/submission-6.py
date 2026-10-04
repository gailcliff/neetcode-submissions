class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = Counter(nums)

        heap = [(val, key) for key, val in counter.items()]
        heapq.heapify(heap)

        while len(heap) > k:
            heapq.heappop(heap)
        
        return [item[1] for item in heap]