from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_area = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    area = 1
                    q = deque([(i, j)])
                    grid[i][j] = 0
                    while q:
                        pi, pj = q.popleft()
                        if pi > 0 and grid[pi-1][pj] == 1:
                            q.append((pi-1, pj))
                            area += 1
                            grid[pi-1][pj] = 0
                        if pi < rows-1 and grid[pi+1][pj] == 1:
                            q.append((pi+1, pj))
                            area += 1
                            grid[pi+1][pj] = 0
                        if pj > 0 and grid[pi][pj-1] == 1:
                            q.append((pi, pj-1))
                            area += 1
                            grid[pi][pj-1] = 0
                        if pj < cols-1 and grid[pi][pj+1] == 1:
                            q.append((pi, pj+1))
                            area += 1
                            grid[pi][pj+1] = 0
                    if area > max_area:
                        max_area = area
        return max_area