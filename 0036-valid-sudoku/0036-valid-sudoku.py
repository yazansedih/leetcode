class Solution(object):
    def isValidSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):

                value = board[row][col]

                # Ignore empty cells
                if value == ".":
                    continue

                # Find the 3x3 box
                box = (row // 3) * 3 + (col // 3)

                # Check duplicate
                if value in rows[row]:
                    return False

                if value in cols[col]:
                    return False

                if value in boxes[box]:
                    return False

                # Add value
                rows[row].add(value)
                cols[col].add(value)
                boxes[box].add(value)

        return True