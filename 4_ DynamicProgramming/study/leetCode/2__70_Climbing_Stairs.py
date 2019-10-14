# 70. Climbing Stairs
# https: // leetcode.com/problems/climbing-stairs/


def power(a, n):
    ret = [[1, 0], [0, 1]]
    while n > 0:
        if n % 2 == 1:
            ret = multiply(ret, a)
            print("return:")
            print(ret)
        print(f'n: {n}')
        n = n // 2
        a = multiply(a, a)
        print("a:")
        print(a)
    return ret


def multiply(a, b):
    c = [[0, 0], [0, 0]]
    for i in range(0, 2):
        for j in range(0, 2):
            c[i][j] = (a[i][0] * b[0][j]) + (a[i][1] * b[1][j])
    return c


class Solution:
    def climbStairs(self, n):
        q = [[1, 1], [1, 0]]
        res = power(q, n)
        return res[0][0]
