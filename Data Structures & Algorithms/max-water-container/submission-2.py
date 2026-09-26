class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            amount = (right - left) * min(heights[left], heights[right])
            maximum = max(maximum, amount)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return maximum