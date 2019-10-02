class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return 0

        dp = [r[:] for r in grid]
        m = len(grid)
        n = len(grid[0])

        dp[0][0] = 1

        for r in range(1, m):
            dp[r][0] = 0 if grid[r][0] == 1 else dp[r-1][0]

        for c in range(1, n):
            dp[0][c] = 0 if grid[0][c] == 1 else dp[0][c-1]

        for r in range(1, m):
            for c in range(1, n):
                dp[r][c] = 0 if grid[r][c] == 1 else dp[r-1][c] + dp[r][c-1]

        # print(r, c, dp)
        return dp[-1][-1]
