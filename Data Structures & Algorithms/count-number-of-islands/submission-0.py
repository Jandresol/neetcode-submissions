class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # given a 2D graph
        directions = [[1, 0], [0,1], [-1, 0], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS):
                return
            if (grid[r][c] == "0"):
                return
            # prevent dfs from visiting again
            grid[r][c] = "0"
            # dfs neighbor
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        # restart the dfs
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    # count islands
                    islands += 1
        return islands


        