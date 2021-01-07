def firstBad(n):
    l = 1; r = n

    while(l<r):
        mid = (l+r) // 2
        if(not isBadVersion(mid)):
            l = mid + 1
        else:
            r = mid
    
    return mid