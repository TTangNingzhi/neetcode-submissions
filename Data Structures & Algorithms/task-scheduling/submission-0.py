import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = [-c for c in Counter(tasks).values()]
        heapq.heapify(heap)
        queue = deque()
        time = 0
        while heap or queue:
            time += 1
            if heap:
                c = heapq.heappop(heap) + 1
                if c:
                    queue.append((c, time + n))
            if queue and queue[0][1] == time:
                heapq.heappush(heap, queue.popleft()[0])
        return time