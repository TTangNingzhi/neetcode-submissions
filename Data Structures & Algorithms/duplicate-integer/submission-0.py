class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_sorted = sorted(nums)
        diffs = [nums_sorted[i+1] - nums_sorted[i] for i in range(len(nums)-1)]
        for diff in diffs:
            if diff == 0:
                return True
        return False