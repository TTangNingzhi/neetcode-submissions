import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [(p[0] ** 2 + p[1] ** 2, p) for p in points]
        heapq.heapify(heap)
        count = 0
        res = []
        while count < k:
            res.append(heapq.heappop(heap)[1])
            count += 1
        return res