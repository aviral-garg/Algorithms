def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def groupTheNumbers(arr):
    evenCount = 0

    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            evenCount += 1

    j = evenCount
    print('j', j)

    i = 0
    while i < evenCount and j < len(arr):
        print('asasdasdds')

        while arr[i] % 2 == 0:
            i += 1
        print(i)

        while j < len(arr) and arr[j] % 2 != 0:
            j += 1
        print(j)

        if i == evenCount or j == len(arr):
            continue

        swap(arr, i, j)


# arr = [3, 7, 1, 2, 4, 8]
arr = [2, 4, 8, 3, 7, 1]
# arr = [3, 5, 4, 6, 7, 8]
groupTheNumbers(arr)
print(arr)
