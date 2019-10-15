def generate_all_expressions(s, target):
    n = len(s)
    test = []
    res = []

    def posRec(i):
        def pre(op):
            n1 = 0
            for j in range(0, i):
                n1 = 10 * n1 + int(s[j])

        def post(op):
            n2 = 0
            for k in range(i, n):
                n2 = 10 * n2 + int(s[k])

        test.append(pre(i) + None + post(i))
        test.append(pre(i) + "+" + post(i))
        test.append(pre(i) + "*" + post(i))

    def getList():
        for a in range()
    x = getList()
    posRec(x)

    return res


print(generate_all_expressions("234", 27))

# if op == None:
#     n1 = pow(10, n-i)*n1+n2
#     if n1 == target:
#         return n1
# elif op == "+" and n1 + n2 == target:
#     return str(n1) + "+" + str(n2)
# elif op == "*" and n1 * n2 == target:
#     return str(n1) + "*" + str(n2)
