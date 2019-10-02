import sys


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        if amount == 0:
            return 0

        dp = [float("inf")]*(amount+1)

        i = 0
        while i <= amount:

            if i in coins:
                dp[i] = 1
                i += 1
                continue

            # get min previous solution
            min_prev_sol = float("inf")
            for c in coins:
                if c < i:
                    min_prev_sol = min(min_prev_sol, dp[i-c])
            dp[i] = min_prev_sol + \
                1 if min_prev_sol != float("inf") else float("inf")

            print(dp)

            i += 1

        return dp[-1] if dp[-1] != float("inf") else -1
