class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])

        dp = [[e for e in row] for row in grid]

        for i in range(1, r):
            dp[i][0] += dp[i-1][0]

        for j in range(1, c):
            dp[0][j] += dp[0][j-1]

        for i in range(1, r):
            for j in range(1, c):
                dp[i][j] += min(dp[i-1][j], dp[i][j-1])

        return dp[-1][-1]
