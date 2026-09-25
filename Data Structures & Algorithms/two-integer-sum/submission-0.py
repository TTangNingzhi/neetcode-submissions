class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        candidates = {}
        for i in range(len(nums)):
            if nums[i] in candidates:
                return [candidates[nums[i]], i]
            candidates[target - nums[i]] = i
        