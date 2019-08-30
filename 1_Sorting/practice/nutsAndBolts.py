from random import randrange


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def partition(arr, lo, hi, p):
    i = lo - 1
    for j in range(lo, hi):
        if arr[i] < p:
            i += 1
            swap(arr, i, j)
        elif arr[i] == p:
            swap(arr, j, hi)

    swap(arr, i, hi)
    return i


def sortNB(nuts, bolts, lo, hi):

    if lo < hi:
        idx = randrange(lo, hi)
        pivot = partition(nuts, lo, hi, bolts[idx])
        partition(bolts, lo, hi, nuts[pivot])

        sortNB(nuts, bolts, lo, pivot-1)
        sortNB(nuts, bolts, pivot+1, hi)


def solve(nuts, bolts):
    lo = 0
    hi = len(nuts) - 1
    sortNB(nuts, bolts, lo, hi)
    print(nuts, bolts)


solve([43, 4, 2, 7], [2, 7, 4, 43])
