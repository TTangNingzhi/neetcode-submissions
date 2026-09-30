class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def isValid(piles, h, k):
            total = 0
            for p in piles:
                total += p // k + (1 if p % k else 0)
            return total <= h

        maximum = max(piles)
        left, right = 1, maximum
        while left < right:
            mid = (left + right) // 2
            if isValid(piles, h, mid):
                right = mid
            else:
                left = mid + 1
        return left