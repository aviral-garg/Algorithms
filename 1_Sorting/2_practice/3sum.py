def TwoSum(arr, lo, hi, target):
    hm = {}
    res = []

    for i in range(lo, hi):
        compliment = hm.get(target - arr[i])
        if compliment is not None:
            a = min(target - arr[i], arr[i])
            b = max(target - arr[i], arr[i])
            res.append(str(a) + "," + str(b))
        else:
            hm[arr[i]] = i

    return res


def findZeroSum(arr):
    arr = arr.sort()
    result = False
    res = []
    s = set()
    for i in range(len(arr)):
        lo, hi = i+1, len(arr)

        comps = TwoSum(arr, lo, hi, -arr[i])
        for e in comps:
            c = (str(arr[i]) + "," + e)
            if c not in s:
                s.add(c)
                res.append(c)
        i += 1
    return res


if __name__ == "__main__":
    # arr = [2, 3, -1, 4, 0, 1, 5]
    # arr = [10, 3, -4, 1, -6, 9]
    arr = [4, -2, -2, -1, -3]
    print(findZeroSum(arr))
