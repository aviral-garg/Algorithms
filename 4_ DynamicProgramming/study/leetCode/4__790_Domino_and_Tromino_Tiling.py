# 790. Domino and Tromino Tiling
# https: // leetcode.com/problems/domino-and-tromino-tiling/


class Solution:
    def numTilings(self, n: int) -> int:
        if n <= 2:
            return n

        f3 = 1
        f2 = 2
        f1 = 5

        for i in range(4, n+1):
            f = 2*f1 + f3

            f3 = f2
            f2 = f1
            f1 = f

        return f1 % (10**9 + 7)
