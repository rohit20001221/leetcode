def fourSum2(A, B, C, D):
    m = {}
    ans = 0

    for x in A:
        for y in B:
            m[x+y] = m.get(x+y, 0) + 1

    for x in C:
        for y in D:
            target = -(x+y)
            ans = m.get(target, 0) + 1

    return ans

print(fourSum2([1,-1,0], [-1,2,1],[1,1,1],[-1,-1,-1]))