class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])
        cs, ce = intervals[0][0], intervals[0][1]
        res = []
        for interval in intervals[1:]:
            if interval[0] <= ce:
                ce = max(interval[1], ce)
            else:
                res.append([cs, ce])
                cs, ce = interval[0], interval[1]
        res.append([cs, ce])
        return res