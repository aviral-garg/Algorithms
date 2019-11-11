# 276. Paint Fence
# https: // www.geeksforgeeks.org/painting-fence-algorithm/

# n = 3, k = 2

# p2 p1 c
# 1  3  red = R
# 1  3  green
# 1  3  blue

# 3
#             sum(p1) - p1[i]
#                 |
# R = prev_R + prev_NOT_R
#       |
#     p1[i] - p2[i]

# n = ?, k = 20
# 1   2
# _____
# 1  20 c1
# 1  20 c2
# 1  20 c3
# 1  20
# 1  20
# 1  20
# .  20
# .  20
# .  20

# n = 4, k = 1
# 0, 1, 2, 3
# 1  1


def numWays(n, k):

    p2 = [1 for _ in range(k)]  # first post to start with
    p1 = [k for _ in range(k)]  # second post to start with
    c = [0 for _ in range(k)]  # third post to start with

    p2Sum = k    # sum(p2)
    p1Sum = k**2  # sum(p1)
    cSum = 0

    for _ in range(2, n+1):
        cSum = 0
        for color in range(k):  # O(k)
            same = p1[color] - p2[color]
            diff = p1Sum - p1[color]
            c[color] = same + diff
            cSum += c[color]

        p2 = p1[:]
        p2Sum = p1Sum
        p1 = c[:]
        p1Sum = cSum

    return p1Sum
