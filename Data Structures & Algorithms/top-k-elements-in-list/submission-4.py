class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1
        
        heap = [] # min heap

        for num, count in counts.items():
            if len(heap) < k:
                heapq.heappush(heap, (count, num))
            else:
                if count > heap[0][0]:
                    heapq.heappushpop(heap, (count, num))
        
        return [item[1] for item in heap]