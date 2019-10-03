# T(N) = O(N) Linear in the magnitude of input
# S(N) = O(N) exponential in size of input log(N)


class Solution:
    def knightDialer(self, N: int) -> int:
        dp = [[0 for _ in range(10)] for _ in range(N+1)]

        for digit in range(10):
            dp[1][digit] = 1

        for i in range(2, N+1):
            dp[i][0] = dp[i-1][4] + dp[i-1][6]
            dp[i][1] = dp[i-1][6] + dp[i-1][8]
            dp[i][2] = dp[i-1][7] + dp[i-1][9]
            dp[i][3] = dp[i-1][4] + dp[i-1][8]
            dp[i][4] = dp[i-1][3] + dp[i-1][9] + dp[i-1][0]
            dp[i][5] = 0
            dp[i][6] = dp[i-1][1] + dp[i-1][7] + dp[i-1][0]
            dp[i][7] = dp[i-1][2] + dp[i-1][6]
            dp[i][8] = dp[i-1][1] + dp[i-1][3]
            dp[i][9] = dp[i-1][2] + dp[i-1][4]

        return sum(dp[N]) % (10**9 + 7)
