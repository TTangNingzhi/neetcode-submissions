class Solution:
    def trap(self, height: List[int]) -> int:
        lmax, rmax = 0, 0
        prefix = [0] * len(height)
        suffix = [0] * len(height)
        for i in range(len(height)):
            lmax = max(lmax, height[i])
            prefix[i] = lmax
            rmax = max(rmax, height[len(height) - 1 - i])
            suffix[len(height) - 1 - i] = rmax
        amount = 0
        for i in range(len(height)):
            amount += min(prefix[i], suffix[i]) - height[i]
        return amount