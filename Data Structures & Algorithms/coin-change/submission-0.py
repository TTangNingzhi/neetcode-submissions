class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = [0] + [-1] * amount
        for i in range(1, amount + 1):
            candidates = [res[i - coin] + 1 for coin in coins if coin <= i and res[i - coin] != -1]
            res[i] = min(candidates) if candidates else -1
        return res[amount]