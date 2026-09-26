class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lmin = prices[0]
        profit = 0
        for i in range(len(prices)):
            if prices[i] > lmin:
                profit = max(profit, prices[i] - lmin)
            else:
                lmin = prices[i]
        return profit