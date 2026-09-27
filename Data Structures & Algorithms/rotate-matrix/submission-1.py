class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # x, y -> y, n - x
        # n = len(matrix) - 1, x = j, y = len(matrix) - 1 - i
        # j, len(matrix) - 1 - i -> len(matrix) - 1 - i, len(matrix) - 1 - j
        # i, j -> j, len(matrix) - 1 - i -> len(matrix) - 1 - i, len(matrix) - 1 - j -> len(matrix) - 1 - j, i -> i, j
        n = len(matrix)
        for i in range(n-1):
            for j in range(i,n-1-i):
                t = matrix[n-1-j][i]
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                matrix[j][n-1-i] = matrix[i][j]
                matrix[i][j] = t
