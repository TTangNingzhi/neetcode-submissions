class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda iv: iv[0])
        ce = intervals[0][1]
        res = 0
        for iv in intervals[1:]:
            if iv[0] < ce:
                ce = min(iv[1], ce)
                res += 1
            else:
                ce = iv[1]
        return res