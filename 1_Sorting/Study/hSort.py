def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


# 1 9 8
# 9 1 8
# 8 1 9
# 1 8 9
def heapify(arr, i, n):
    largest = i

    l = 2*i + 1
    r = 2*i + 2

    if l <= n and arr[l] > arr[i]:
        largest = l

    if r <= n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        swap(arr, i, largest)
        heapify(arr, largest, n)


def hSort(arr):

    n = len(arr) - 1
    for i in range(n, -1, -1):
        heapify(arr, i, n)

    m = len(arr)-1
    for i in range(m, -1, -1):
        swap(arr, 0, n)
        n -= 1
        heapify(arr, 0, n)


arr = [3, 10, 1, 7, 15, 8, 5]
# arr = [10, 3, 1]
print(arr)
hSort(arr)
print(arr)

# if __name__ == "__main__":
#     # input
#     arr2D = [[], [1], [2, 2], [10, 7, 8, 2, 1, 5],
#              [1, 1, 1], [10, 3, 1], [3, 10, 1, 7, 15, 8, 5]]
#     print(arr2D)

#     # process
#     for arr in arr2D:
#         hSort(arr)

#     # output
#     print(arr2D)
#     assert arr2D == [[], [1], [2, 2], [
#         1, 2, 5, 7, 8, 10], [1, 1, 1], [1, 3, 10], [1, 3, 5, 7, 8, 10, 15]]
