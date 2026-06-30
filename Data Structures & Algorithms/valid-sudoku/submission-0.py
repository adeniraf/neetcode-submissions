class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = defaultdict(set)
        rows = defaultdict(set)
        grids = defaultdict(set)


        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                if board[i][j] == ".":
                    continue

                if (
                    board[i][j] in rows[i] or
                    board[i][j] in columns[j] or 
                    board[i][j] in grids[(i // 3, j // 3)]
                ):
                    return False
                else:
                    # add to row hashmap
                    rows[i].add(board[i][j])
                    columns[j].add(board[i][j])
                    grids[(i // 3, j // 3)].add(board[i][j])
        return True
                