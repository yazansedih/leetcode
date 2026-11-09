class Solution(object):
    def solve(self, board):

        rows = len(board)
        cols = len(board[0])

        def dfs(i, j):

            # Check boundaries
            if (i < 0 or i >= rows or
                j < 0 or j >= cols or
                board[i][j] != "O"):
                return

            # Mark as safe
            board[i][j] = "#"

            # Explore four directions
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        # 1. Start DFS from boundary O's

        for i in range(rows):
            dfs(i, 0)
            dfs(i, cols - 1)

        for j in range(cols):
            dfs(0, j)
            dfs(rows - 1, j)

        # 2. Process the entire board

        for i in range(rows):
            for j in range(cols):

                if board[i][j] == "O":
                    board[i][j] = "X"

                elif board[i][j] == "#":
                    board[i][j] = "O"