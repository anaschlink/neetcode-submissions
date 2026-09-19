from collections import Counter, deque 
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dic_tasks = Counter(tasks)
        heap = []
        queue = deque()
        time = 0
        for task, counter in dic_tasks.items():
            heapq.heappush(heap,(-counter, task))

        while heap or queue:
            while queue and queue[0][2] == time:
                task_queue = queue.popleft()
                if task_queue[1] != 0:
                    heapq.heappush(heap,(task_queue[1], task_queue[0]))
            if heap:
                task_heap = heapq.heappop(heap)
                return_time = time + n + 1
                new_counter = task_heap[0] + 1
                if new_counter != 0:
                    queue.append((task_heap[1],new_counter, return_time ))

        
            time+=1

        return time
        