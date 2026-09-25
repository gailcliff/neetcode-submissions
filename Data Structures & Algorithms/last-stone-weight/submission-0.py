class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for stone in stones:
            heapq.heappush(heap, -stone)
        
        while len(heap) > 1:
            x, y = heapq.heappop(heap), heapq.heappop(heap)

            if x == y:
                continue
            else:
                heapq.heappush(heap, -abs(x - y))
        
        return -heap[0] if heap else 0