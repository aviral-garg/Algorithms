# fibonacci problem
# 1/2 step climb problem
# 2-row honeyComb problem


def fibonacci(n):
    table = [0]*(n+1)
    table[0] = 0
    table[0] = 1

    for i in range(2, n):
        table[i] = table[i-1] + table[i-2]

    return table[n]


fibonacci(5)
