
class Solution(object):
    def orangesRotting(self, grid):
        ans = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        queue = deque()
        visited = set()
        fresh = 0
        minutes = -1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        def get_neighbors(cell):
            neighbors = []
            cell_r, cell_c = cell
            for dr, dc in directions:
                nr = cell_r + dr
                nc = cell_c + dc
                if (nr >= 0) and (nr < ROWS) and (nc >= 0) and (nc < COLS):
                    if grid[nr][nc] == 1:
                        neighbors.append((nr, nc))
            return neighbors


        while len(queue) > 0:
            # new layer
            for _ in range(len(queue)):
                node = queue.popleft()
                for neighbor in get_neighbors(node):
                    if neighbor in visited:
                        continue
                    nr, nc = neighbor
                    grid[nr][nc] = 2
                    fresh -= 1
                    visited.add(neighbor)
                    queue.append(neighbor)
            minutes += 1

        return minutes if fresh == 0 else -1
