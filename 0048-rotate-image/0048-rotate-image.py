
class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)

        # Step 1: Transpose the matrix
        for row in range(n):
            for col in range(row + 1, n):
                matrix[row][col], matrix[col][row] = (
                    matrix[col][row], matrix[row][col]
                )

        # Step 2: Reverse each row
        for row in matrix:
            row.reverse()
