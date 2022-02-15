def polyEval(poly, x):
    res = 0
    for i in range(len(poly)):
        res += (x**i)*poly[i]
    return res

def polySum(poly1, poly2):
    a = len(poly1)
    b = len(poly2)
    if (a>b):
        c = a
    else:
        c = b
    polynew = []
    for i in range(c):
        new = poly1[i]+poly2[i]
        polynew.append(new)
    for i in polynew:
        last = polynew[-1]
        if last == 0:
            polynew.pop(-1)
    return polynew


def polyMultiply(poly1, poly2):
    res = [0] * (len(poly1) + len(poly2) - 1)
    for o1, i1 in enumerate(poly1):
        for o2, i2 in enumerate(poly2):
            res[o1 + o2] += i1 * i2
    return res




