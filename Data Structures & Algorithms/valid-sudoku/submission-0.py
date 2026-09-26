class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_states = {row: [0] * 9 for row in range(9)}
        col_states = {col: [0] * 9 for col in range(9)}
        sub_states = {(row, col): [0] * 9 for row in range(3) for col in range(3)}
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                digit = int(board[row][col]) - 1
                row_states[row][digit] += 1
                col_states[col][digit] += 1
                sub_states[row // 3, col // 3][digit] += 1
                if row_states[row][digit] > 1 or col_states[col][digit] > 1 or sub_states[row // 3, col // 3][digit] > 1:
                    return False

        return True