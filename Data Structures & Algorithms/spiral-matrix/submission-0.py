class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        left, right, top, bottom = 0, n-1, 0, m-1
        i, j = 0, 0
        result = []
        direction = "right"
        while left <= right and top <= bottom:
            result.append(matrix[i][j])
            if direction == "right":
                if j == right:
                    top += 1
                    direction = "down"
                    i += 1
                else:
                    j += 1
            elif direction == "down":
                if i == bottom:
                    right -= 1
                    direction = "left"
                    j -= 1
                else:
                    i += 1
            elif direction == "left":
                if j == left:
                    bottom -= 1
                    direction = "up"
                    i -= 1
                else:
                    j -= 1
            elif direction == "up":
                if i == top:
                    left += 1
                    direction = "right"
                    j += 1
                else:
                    i -= 1
        return result