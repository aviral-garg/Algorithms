class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[0]*(len(triangle)) for r in range(2)]
        dp[0][0] = triangle[0][0]
        for i in range(1, len(triangle)):
            for j in range(0, len(triangle[i])):
                # print(dp)
                if j == 0:
                    dp[i % 2][j] = triangle[i][j] + dp[(i-1) % 2][0]
                elif j == len(triangle[i])-1:
                    dp[i % 2][j] = triangle[i][j] + dp[(i-1) % 2][j-1]
                else:
                    dp[i % 2][j] = triangle[i][j] + \
                        min(dp[(i-1) % 2][j-1], dp[(i-1) % 2][j])
                # print(dp)
        return min(dp[(len(triangle)+1) % 2])
