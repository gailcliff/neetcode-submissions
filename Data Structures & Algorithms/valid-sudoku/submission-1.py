"""
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]
 ]
"""
from collections import defaultdict
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check of rows are valid
        for row in board:
            filtered_row = [item for item in row if item != '.']
            row_unique = set(filtered_row)

            if len(filtered_row) != len(row_unique):
                return False
        
        # check if columns are valid
        for col in zip(*board):
            filtered_column = [item for item in col if item != '.']
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

                if item != '.':
                    subboxes[(row_group, col_group)].append(item)

                j += 1
            i += 1
        
        for subbox in subboxes.values():
            subbox_unique = set(subbox)
            if len(subbox) != len(subbox_unique):
                return False
        
        return True