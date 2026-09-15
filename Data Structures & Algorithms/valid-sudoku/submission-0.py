class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check of rows are valid
        for row in board:
            filtered_row = []

            for item in row:
                try:
                    filtered_row.append(int(item))
                except:
                    pass

            row_unique = set(filtered_row)
            if len(filtered_row) != len(row_unique):
                return False
        
        # check if columns are valid
        for col in zip(*board):
            filtered_column = []

            for item in col:
                try:
                    filtered_column.append(int(item))
                except:
                    pass

            col_unique = set(filtered_column)
            if len(filtered_column) != len(col_unique):
                return False
        
        # check if sub-boxes are valid
        subboxes = defaultdict(list)

        for i in range(9):
            for j in range(9):
                row_group = (i // 3) * 3
                col_group = (j // 3) * 3

                item = board[i][j]

                try:
                    subboxes[(row_group, col_group)].append(int(item))
                except:
                    pass
                j += 1
            i += 1
        
        for subbox in subboxes.values():
            subbox_unique = set(subbox)
            if len(subbox) != len(subbox_unique):
                return False
        
        return True
            
