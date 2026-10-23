class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        cs, ce = newInterval
        inserted = False
        for interval in intervals:
            if interval[1] < newInterval[0]:
                res.append(interval)
            elif interval[0] <= newInterval[1]:
                cs = min(interval[0], cs)
                ce = max(interval[1], ce)
            else:
                if not inserted:
                    res.append([cs, ce])
                    inserted = True
                res.append(interval)
        if not inserted:
            res.append([cs, ce])
            inserted = True
        return res