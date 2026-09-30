class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[left]:
                right = mid
            else:
                if nums[right] < nums[mid]:
                    left = mid + 1
                else:
                    right = left
        return nums[right]