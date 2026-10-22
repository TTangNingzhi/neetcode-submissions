from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    count += 1
                    q = deque([(i, j)])
                    grid[i][j] = "0"
                    while q:
                        pi, pj = q.popleft()
                        if pi > 0 and grid[pi-1][pj] == "1":
                            q.append((pi-1, pj))
                            grid[pi-1][pj] = "0"
                        if pi < rows-1 and grid[pi+1][pj] == "1":
                            q.append((pi+1, pj))
                            grid[pi+1][pj] = "0"
                        if pj > 0 and grid[pi][pj-1] == "1":
                            q.append((pi, pj-1))
                            grid[pi][pj-1] = "0"
                        if pj < cols-1 and grid[pi][pj+1] == "1":
                            q.append((pi, pj+1))
                            grid[pi][pj+1] = "0"
        
        return count