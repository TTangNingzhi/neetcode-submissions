class Solution:
    def rob(self, nums: List[int]) -> int:
        res = [0, nums[0]]
        for i in range(1, len(nums)):
            res.append(max(res[i], res[i-1] + nums[i]))
        return res[len(nums)]