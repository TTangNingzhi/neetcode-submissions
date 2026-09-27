class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero_row, zero_col = set(), set()
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_row.add(i)
                    zero_col.add(j)
        for i in zero_row:
            for j in range(n):
                matrix[i][j] = 0
        for j in zero_col:
            for i in range(m):
                matrix[i][j] = 0