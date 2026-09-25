class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []

        for i in range(len(points)):
            point = points[i]

            distance = -((point[0] ** 2) + (point[1] ** 2))

            if i < k:
                heapq.heappush(heap, (distance, point))
            else:
                if distance > heap[0][0]:
                    heapq.heappushpop(heap, (distance, point))
        
        return [point[1] for point in heap]