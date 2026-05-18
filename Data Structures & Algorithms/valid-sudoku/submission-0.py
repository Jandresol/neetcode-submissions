class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squares = defaultdict(set)
        rows = defaultdict(set)
        columns = defaultdict(set)

        for row in range(9):
            for col in range(9):
                square_index = (row//3) * 3 + (col//3)
                if board[row][col] == ".":
                    continue
                if (board[row][col] in rows[row] or
                    board[row][col] in columns[col] or
                    board[row][col] in squares[square_index]):
                    return False
                rows[row].add(board[row][col])
                columns[col].add(board[row][col])
                squares[square_index].add(board[row][col])
        return True
        