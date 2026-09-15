class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLUMNS = len(matrix[0])

        l, r = 0, (ROWS * COLUMNS) - 1

        while l <= r:
            mid = (l + r) // 2

            row = mid // COLUMNS
            col = mid % COLUMNS

            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                r = mid - 1
            else:
                l = mid + 1
        
        return False