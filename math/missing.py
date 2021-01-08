def missingNumber(arr):
    n = len(arr)
    s_ = sum(arr)
    s = n*(n+1)/2

    return s-s_

print(missingNumber([0,1,2,3,5,6]))