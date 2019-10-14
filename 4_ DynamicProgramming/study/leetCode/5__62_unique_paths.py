class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for _i in range(m)] for _j in range(n)]
        for r in range(1, n):
            for c in range(1, m):
                dp[r][c] = dp[r-1][c] + dp[r][c-1]
        return dp[-1][-1]
