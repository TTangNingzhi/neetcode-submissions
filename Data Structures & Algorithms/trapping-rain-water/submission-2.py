class Solution:
    def trap(self, height: List[int]) -> int:
        box = [0] * len(height)
        box[0] = height[0]
        box[len(height) - 1] = height[len(height) - 1]
        left = 1
        right = len(height) - 2
        while left <= right:
            if height[left] >= box[left - 1]:
                box[left] = height[left]
                left += 1
            elif height[right] >= box[right + 1]:
                box[right] = height[right]
                right -= 1
            else:
                if box[left - 1] <= box[right + 1]:
                    box[left] = box[left - 1]
                    left += 1
                else:
                    box[right] = box[right + 1]
                    right -= 1
        return sum(box) - sum(height)
