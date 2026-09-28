class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        counter = Counter(tasks)
        heap = [-count for count in counter.values()]
        heapq.heapify(heap)

        task_queue = deque()

        time = 0
        while heap or task_queue:
            time += 1
            
            if heap:
                next_in_heap = heapq.heappop(heap)
                next_in_heap += 1
                
                if next_in_heap != 0:
                    task_queue.append((next_in_heap, time + n))
            
            if task_queue and task_queue[0][1] == time:
                next_in_queue, _ = task_queue.popleft()
                heapq.heappush(heap, next_in_queue)
        
        return time
