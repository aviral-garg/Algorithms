def heapify(arr, hi, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < hi and arr[l] > arr[largest]:
        largest = l

    if r < hi and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, hi, largest)


def hSort(arr):

    hi = len(arr)
    for i in range(hi, -1, -1):
        heapify(arr, hi, i)

    for i in range(hi-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)


arr = [10, 3, 4, 7, 2, 0, -1, 4, -2]
hSort(arr)
print(arr)
