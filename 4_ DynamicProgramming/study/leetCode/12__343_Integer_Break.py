# 343. Integer Break
# https://leetcode.com/problems/integer-break/


class Solution:
    def integerBreak(self, n: int) -> int:

        if n < 2:
            return 0

        #          0, 1
        product = [0, 1, ]

        for i in range(2, n+1):
            product.append(1)

            product[i] = max(product[i], product[i//2] *
                             product[i-i//2], i//2*(i-i//2))

        # print(product)
        return product[n]
