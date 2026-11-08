class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        m = len(grid)
        n = len(grid[0])
        count = 0

        def dfs(i, j):
            # Check boundaries
            if i < 0 or i >= m or j < 0 or j >= n:
                return

            # Stop if water or already visited
            if grid[i][j] == "0":
                return

            # Mark land as visited
            grid[i][j] = "0"

            # Explore four directions
            dfs(i - 1, j)  # Up
            dfs(i + 1, j)  # Down
            dfs(i, j - 1)  # Left
            dfs(i, j + 1)  # Right

        # Traverse the entire grid
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)

        return count