class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        counter = Counter(tasks)
        heap = [-count for count in counter.values()]
        heapq.heapify(heap)

        cooldown_pending = deque()

        time = 0
        while heap or cooldown_pending:
            time += 1

            if heap:
                curr_task_remaining = heapq.heappop(heap)
                curr_task_remaining += 1

                if curr_task_remaining != 0:
                    cooldown_pending.append(
                        (curr_task_remaining, time + n)
                    )
            
            if cooldown_pending and time == cooldown_pending[0][1]:
                task_cycles, _ = cooldown_pending.popleft()
                heapq.heappush(heap, task_cycles)
        
        return time