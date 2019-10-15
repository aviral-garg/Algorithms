# 983. Minimum Cost For Tickets
# https://leetcode.com/problems/minimum-cost-for-tickets/


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0 for _ in days]
        dp[0] = min(costs)

        def get_last_cost(i, pass_days):
            j = i-1
            while j >= 0 and days[j] >= days[i]-(pass_days-1):
                j -= 1

            if j >= 0:
                return dp[j]
            else:
                return 0

        for i in range(1, len(days)):
            cases = [c for c in costs]
            cases[0] += get_last_cost(i, 1)
            cases[1] += get_last_cost(i, 7)
            cases[2] += get_last_cost(i, 30)
            print(cases)
            dp[i] = min(cases)

        return dp[-1]
