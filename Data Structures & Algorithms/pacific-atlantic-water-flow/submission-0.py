class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        def dfs(r, c, visit, prevHeight):
            if ((r, c) in visit or
            r < 0 or c < 0 or
            r == ROWS or c == COLS or
            # here, we stop if the new cell is less
            # than the previous cell
            #we start at the border cells and go 
            # in if it is >=
            heights[r][c] < prevHeight):
                return  
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])
        
        # start at the border cells 
        for c in range(COLS):
            # left side is pacific
            dfs(0, c, pac, heights[0][c])
            # right side is atlantic
            dfs(ROWS -1, c, atl, heights[ROWS-1][c])

        for r in range(ROWS):
            #top side is pacific
            dfs(r, 0, pac, heights[r][0])
            # bottom side is atlantic
            dfs(r, COLS - 1, atl, heights[r][COLS-1])

        # after DFS

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res


        
                        