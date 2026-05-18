class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])

        def getNeighbors(row, col):
            res = []
            directions = [(0,1), (1,0), (0,-1), (-1,0)]
            for dx, dy in directions:
                newRow = row + dx
                newCol = col + dy
                if 0 <= newRow < ROWS and 0 <= newCol < COLS:
                    res.append((newRow, newCol))
            return res

        # BFS
        def bfs(row, col):
            queue = deque([(row, col, 0)])
            visited = set([(row, col)])
            while queue:
                row, col, dist = queue.popleft()
                if grid[row][col] == 0:
                    return dist
                for nx, ny in getNeighbors(row, col):
                    if (nx, ny) not in visited and grid[nx][ny] != -1:
                        visited.add((nx, ny))
                        queue.append((nx, ny, dist + 1))
            return 2**31-1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2**31-1:
                    grid[r][c] = bfs(r, c)
