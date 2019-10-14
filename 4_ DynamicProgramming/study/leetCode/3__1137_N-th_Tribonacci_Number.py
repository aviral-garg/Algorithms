# 1137. N-th Tribonacci Number
# https: // leetcode.com/problems/n-th-tribonacci-number/


class Solution:
    def tribonacci(self, n: int) -> int:
        x = 0
        if n == 0:
            return x
        y = 1
        if n == 1:
            return y
        z = 1
        if n == 2:
            return z

        for i in range(3, n+1):
            a = x + y + z
            x = y
            y = z
            z = a

        return a
