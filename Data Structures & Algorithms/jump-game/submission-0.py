class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = [False] * len(nums)
        reach[0] = True
        for i in range(len(nums)):
            if reach[i]:
                for j in range(1, nums[i] + 1):
                    if i+j < len(nums):
                        reach[i+j] = True
            else:
                break
        return reach[len(nums)-1]