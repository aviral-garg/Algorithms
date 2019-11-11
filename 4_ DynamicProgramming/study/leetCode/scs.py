class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        row = len(str2)
        col = len(str1)
        # Edit Distance
        dp = [[0 for c in range(col+1)] for r in range(row+1)]
        for r in range(1, row+1):
            for c in range(1, col+1):
                m = 1 if str1[c-1] == str2[r-1] else 0
                dp[r][c] = max(dp[r-1][c] + 1, dp[r][c-1] + 1, dp[r-1][c-1]+m)
        # traceback
        str3 = []
        r = len(str2)
        c = len(str1)
        while r != 0 and c != 0:
            if dp[r][c] == dp[r-1][c]:
                str3.append(str2[r-1])
                r -= 1
            elif dp[r][c] == dp[r][c-1]:
                str3.append(str1[c-1])
                c -= 1
            else:
                str3.append(str1[c-1])
                r -= 1
                c -= 1
        while r != 0:
            str3.append(str2[r-1])
            r -= 1
        while c != 0:
            str3.append(str1[c-1])
            c -= 1
        str3.reverse()
        return "".join(str3)
