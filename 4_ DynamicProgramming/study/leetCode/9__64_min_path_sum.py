# Space Optimized DP solution T=O(m+n) S=O(n)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0

        p_row = [c for c in grid[0]]
        row = p_row[:]

        for c in range(1, len(grid[0])):
            p_row[c] += p_row[c-1]

        for r in range(1, len(grid)):
            row = grid[r][:]
            row[0] += p_row[0]

            for c in range(1, len(grid[0])):
                row[c] += min(row[c-1], p_row[c])

            p_row = row[:]

        return p_row[-1]

# normal dp solution T=O(m+n) S=O(m+n)
# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:
#         r = len(grid)
#         c = len(grid[0])

#         dp = [[e for e in row] for row in grid]

#         for i in range(1, r):
#             dp[i][0] += dp[i-1][0]

#         for j in range(1, c):
#             dp[0][j] += dp[0][j-1]

#         for i in range(1, r):
#             for j in range(1, c):
#                 dp[i][j] += min(dp[i-1][j], dp[i][j-1])

#         return dp[-1][-1]
