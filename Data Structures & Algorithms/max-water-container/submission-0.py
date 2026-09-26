class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            amount = (right - left) * min(heights[left], heights[right])
            maximum = max(maximum, amount)
            left_next = left + 1
            while left_next < right and heights[left_next] <= heights[left]:
                left_next += 1
            right_next = right - 1
            while left < right_next and heights[right_next] <= heights[right]:
                right_next -= 1
            if heights[left] < heights[right]:
                left = left_next
            elif heights[left] > heights[right]:
                right = right_next
            else:
                left = left_next
                right = right_next
        return maximum