class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        li, lj = 0, 0
        ri, rj = m-1, n-1
        while li < ri or li == ri and lj <= rj:
            d = (ri - li) * n + rj - lj
            mi = li + (lj + d // 2) // n
            mj = (lj + d // 2) % n
            if matrix[mi][mj] == target:
                return True
            elif matrix[mi][mj] < target:
                li = mi + (mj + 1) // n
                lj = (mj + 1) % n
            else:
                ri = mi + (mj - 1) // n
                rj = (mj - 1) % n
        return False