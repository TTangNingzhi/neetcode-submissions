import copy

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            new = [copy.deepcopy(e) for e in res]
            for e in new:
                e.append(num)
            res.extend(new)
        return res
            