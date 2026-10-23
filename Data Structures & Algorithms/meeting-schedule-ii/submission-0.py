"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda iv: iv.start)
        heap = []
        res = 0
        for iv in intervals:
            while heap and heap[0] <= iv.start:
                heapq.heappop(heap)
            heapq.heappush(heap, iv.end)
            res = max(len(heap), res)
        return res