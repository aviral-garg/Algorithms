# T(N) = O(N) Linear in the magnitude of input
# S(N) = O(N) exponential in size of input log(N)


class Solution:
    def knightDialer(self, N: int) -> int:
        prev = [1]*10  # for N = 1
        curr = [1]*10

        for i in range(2, N+1):
            curr[0] = prev[4] + prev[6]
            curr[1] = prev[6] + prev[8]
            curr[2] = prev[7] + prev[9]
            curr[3] = prev[4] + prev[8]
            curr[4] = prev[3] + prev[9] + prev[0]
            curr[5] = 0
            curr[6] = prev[1] + prev[7] + prev[0]
            curr[7] = prev[2] + prev[6]
            curr[8] = prev[1] + prev[3]
            curr[9] = prev[2] + prev[4]
            prev = curr[:]
        return sum(curr) % (10**9 + 7)
