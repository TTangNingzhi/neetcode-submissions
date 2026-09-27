class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        cur = n
        while True:
            if cur == 1:
                return True
            if cur in seen:
                return False
            else:
                n = 0
                seen.add(cur)
                while cur:
                    n += (cur % 10) ** 2
                    cur = cur // 10
                cur = n

