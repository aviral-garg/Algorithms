# Space Optimized DP solution T=O(m+n) S=O(n)
class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        if len(grid[0]) == 0:
            return 1

        p_row = [0 for _ in grid[0]]
        row = p_row[:]

        for c in range(len(grid[0])):
            if grid[0][c] != 1:
                p_row[c] = 1
            else:
                break

        print(p_row)
        for r in range(1, len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    if c == 0:
                        row[c] = p_row[c]
                    else:
                        row[c] = row[c-1] + p_row[c]
                else:
                    row[c] = 0
            p_row = row[:]
            print(row)

        return p_row[-1]

# normal dp solution T=O(m+n) S=O(m+n)
# class Solution:
#     def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
#         if grid[0][0] == 1:
#             return 0

#             dp = [r[:] for r in grid]
#             m = len(grid)
#             n = len(grid[0])

#         dp[0][0] = 1

#         for r in range(1, m):
#             dp[r][0] = 0 if grid[r][0] == 1 else dp[r-1][0]

#         for c in range(1, n):
#             dp[0][c] = 0 if grid[0][c] == 1 else dp[0][c-1]

#         for r in range(1, m):
#             for c in range(1, n):
#                 dp[r][c] = 0 if grid[r][c] == 1 else dp[r-1][c] + dp[r][c-1]

#         return dp[-1][-1]

        # alternative:
        #
        # if grid[0][0] == 1:
        #     return 0

        # dp = [[0 for _ in row] for row in grid]

        # r = len(grid)
        # c = len(grid[0])

        # i = 0
        # while i < c and grid[0][i] != 1:
        #     dp[0][i] = 1
        #     i += 1

        # i = 0
        # while i < r and grid[i][0] != 1:
        #     dp[i][0] = 1
        #     i += 1

        # for i in range(1, r):
        #     for j in range(1, c):
        #         if grid[i][j] != 1:
        #             dp[i][j] = dp[i-1][j] + dp[i][j-1]

        # return dp[-1][-1]
