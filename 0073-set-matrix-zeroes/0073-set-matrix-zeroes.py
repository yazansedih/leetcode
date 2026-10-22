class Solution(object):
    def setZeroes(self, matrix):

        zero_rows = set()
        zero_cols = set()

        rows = len(matrix)
        cols = len(matrix[0])

        # Find all original zero positions
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    zero_rows.add(row)
                    zero_cols.add(col)

        # Set rows to zero
        for row in zero_rows:
            for col in range(cols):
                matrix[row][col] = 0

        # Set columns to zero
        for col in zero_cols:
            for row in range(rows):
                matrix[row][col] = 0

        return True
                
