# assumption: 1 <= arr[i] <= 9


def bSort(arr):
    count = {}
    for e in arr:
        count[e] = 1 if count.get(e) == None else count[e] + 1

    j = 0
    for i in range(1, 9):
        val = count.get(i)
        if val != None:
            for k in range(val):
                arr[j] = i
                j += 1

    return arr


print(bSort([4, 3, 1, 4, 2, 4, 2]))
