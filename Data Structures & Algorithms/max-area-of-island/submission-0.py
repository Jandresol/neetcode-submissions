class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1,0], [0,1], [-1, 0], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        max_area = 0

        def dfs(r, c):
            
            # base case
            if (r >= ROWS or c >= COLS or r < 0 or c < 0 
                or grid[r][c] == 0):
                return 0
            # mark as visited
            grid[r][c] = 0
            area = 1
            
            # for neighbor in neighbor add 1
            # got stuck here, everything else was
            # by myself
            for dr, dc in directions:
                area += dfs(r + dr, c + dc)
            return area
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))

        return max_area
    