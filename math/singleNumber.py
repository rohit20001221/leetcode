def singleNumber(arr):
    return 2*sum(set(arr)) - sum(arr)