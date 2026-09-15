class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        # treating the 2D array as one long 1D array
        l, r = 0, (ROWS * COLS) - 1

        while l <= r:
            mid_1d_idx = (l + r) // 2

            row = mid_1d_idx // COLS
            col = mid_1d_idx % COLS
            # reverse mapping for mid_1d_idx is row * COLS + col

            if target == matrix[row][col]:
                return True
            elif target <= matrix[row][col]:
                r = mid_1d_idx - 1
            else:
                l = mid_1d_idx + 1
        
        return False


        