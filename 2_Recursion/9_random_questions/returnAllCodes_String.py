def get_hash_map():
    # create a map of int -> char
    # that looks like: {1: 'a', 2: 'b' ... 25: 'y', 26: 'z'}
    for i in range(ord("a"), ord("z")+1):
        hashMap[i - ord("a") + 1] = chr(i)


def get_codes(prefix, i, res, s, m):
    return res


def returnAllCodes(s):
    res = []
    hashMap = {}

    m = get_hash_map()

    res = get_codes("", 0, res, s, hashMap)
    print(res)
    # get_codes(prefix, i, s, m)

    return res


print(returnAllCodes(1123))
