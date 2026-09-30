class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[left]:
                right = mid
            else:
                if nums[left] < nums[right]:
                    right = left
                else:
                    left = mid + 1
        index_min = left

        if index_min == 0 or target < nums[0]:
            left, right = index_min, len(nums) - 1
        else:
            left, right = 0, index_min - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1