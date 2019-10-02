class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # setup the cache table
        num = [[0] * n for _ in range(m)]

        # fill the cache table
        for r in range(0, m):
            for c in range(0, n):
                num[r][c] = 1 if r == 0 or c == 0 else num[r-1][c] + num[r][c-1]

        # result
        return num[m-1][n-1]
