def lexicographical_order(arr):
    hm1 = {}
    hm2 = {}

    for e in arr:
        key = e.split(" ")[0]
        value = e.split(" ")[1]

        if hm1.get(key) == None:
            hm1[key] = 1
            hm2[key] = value
        else:
            hm1[key] += 1
            hm2[key] = value if hm2[key] < value else hm2[key]

    res = []
    for k, v in hm1.items():
        res.append(k + ":" + str(v) + "," + hm2[k])

    return res


print(lexicographical_order(["a 11a", "a z2"]))
