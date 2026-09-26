class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        i = 0
        results = set()
        while i < len(nums) - 2:
            target = 0 - nums[i]
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[j] + nums[k] < target:
                    j += 1
                elif nums[j] + nums[k] > target:
                    k -= 1
                else:
                    results.add((nums[i], nums[j], nums[k]))
                    j += 1
            i += 1
        results = [list(result) for result in results]
        return results