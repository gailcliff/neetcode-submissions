class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = defaultdict(set)
        columns = defaultdict(set)
        grids = defaultdict(set)

        N = len(board)

        for i in range(N):
            for j in range(N):
                item = board[i][j]
                if item == '.': continue

                if (item in rows[i] or
                    item in columns[j] or
                    item in grids[(i // 3, j // 3)]):
                    # O(1) lookup
                    return False
                
                rows[i].add(item)
                columns[j].add(item)
                grids[(i // 3, j // 3)].add(item)
        
        return True