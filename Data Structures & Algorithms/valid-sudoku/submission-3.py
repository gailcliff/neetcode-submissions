class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        sub_grids = defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board)):
                item = board[row][col]

                if item == '.':
                    continue

                if (
                    item in rows[row] 
                    or item in cols[col]
                    or item in sub_grids[(row // 3, col // 3)]
                ):
                    return False
            
                rows[row].add(item)
                cols[col].add(item)
                sub_grids[(row//3, col//3)].add(item)
        
        return True
        