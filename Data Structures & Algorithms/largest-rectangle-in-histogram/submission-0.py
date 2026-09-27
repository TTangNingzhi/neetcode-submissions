class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        def next_and_prev_smaller(nums: List[int]) -> (List[int], List[int]):
            next_smaller = [len(nums)] * len(nums)
            prev_smaller = [-1] * len(nums)
            stack = []
            for i, x in enumerate(nums):
                while stack and nums[stack[-1]] > x:
                    next_smaller[stack[-1]] = i
                    stack.pop()
                if stack:
                    prev_smaller[i] = stack[-1]
                stack.append(i)
            return next_smaller, prev_smaller
        
        next_lower, prev_lower = next_and_prev_smaller(heights)
        largest = 0
        for i, h in enumerate(heights):
            largest = max(largest, h * (next_lower[i] - prev_lower[i] - 1))
        return largest
