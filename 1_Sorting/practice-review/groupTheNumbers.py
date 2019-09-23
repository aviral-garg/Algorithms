def getLo(arr, lo, hi):
    while lo < hi and arr[lo] % 2 == 0:
        lo += 1
    return lo


def getHi(arr, lo, hi):
    while lo < hi and arr[hi] % 2 != 0:
        hi -= 1
    return hi


def swap(arr, lo, hi):
    arr[lo], arr[hi] = arr[hi], arr[lo]


def groupTheNumbers(arr):
    lo, hi = 0, len(arr) - 1
    while lo < hi:
        lo = getLo(arr, lo, hi)
        hi = getHi(arr, lo, hi)
        swap(arr, lo, hi)

    return arr


arr = groupTheNumbers([1, 2, 3])
print(arr)
arr = groupTheNumbers([1])
print(arr)
arr = groupTheNumbers([])
print(arr)
arr = groupTheNumbers([1, 1, 1])
print(arr)
arr = groupTheNumbers([2, 2, 2])
print(arr)
