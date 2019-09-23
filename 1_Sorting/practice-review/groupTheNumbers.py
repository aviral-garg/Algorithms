def groupTheNumbers(arr):
    lo, hi = 0, len(arr) - 1
    while lo < hi:
        while lo < hi and arr[lo] % 2 == 0:
            lo += 1
        while lo < hi and arr[hi] % 2 != 0:
            hi -= 1
        if lo < hi:
            arr[lo], arr[hi] = arr[hi], arr[lo]

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
