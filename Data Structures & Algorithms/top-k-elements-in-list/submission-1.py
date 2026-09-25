class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        counts = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for num in counts:
            buckets[counts[num]].append(num)
        res = []
        for i in range(len(nums), 0, -1):
            res.extend(buckets[i])
            if len(res) == k:
                return res