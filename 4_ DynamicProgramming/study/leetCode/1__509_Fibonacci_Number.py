# https: // leetcode.com/problems/fibonacci-number/


class Solution:
    def fib(self, N: int) -> int:
        prev_prev = 0
        if N == 0:
            return prev_prev

        prev = 1
        if N == 1:
            return prev

        for i in range(2, N+1):
            curr = prev + prev_prev
            prev_prev = prev
            prev = curr

        return prev
