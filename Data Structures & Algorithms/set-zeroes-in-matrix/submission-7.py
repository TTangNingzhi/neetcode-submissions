class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        zero_1st_row, zero_1st_col = False, False
        for i in range(0, m):
            for j in range(0, n):
                if matrix[i][j] == 0:
                    if i == 0:
                        zero_1st_row = True
                    else:
                        matrix[i][0] = 0
                    if j == 0:
                        zero_1st_col = True
                    else:
                        matrix[0][j] = 0
        
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0

        if zero_1st_row:
            for j in range(0, n):
                matrix[0][j] = 0
        if zero_1st_col:
            for i in range(0, m):
                matrix[i][0] = 0