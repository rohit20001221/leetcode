def qsort(arr):
    qsortHelper(arr, 0, len(arr)-1)

def qsortHelper(arr, l, r):
    if(l < r):
        pIndex = partition(arr, l, r)
        qsortHelper(arr, l, pIndex-1)
        qsortHelper(arr, pIndex+1, r)

def partition(arr, l, r):
    pivot = arr[r]
    pIndex = l

    for i in range(l, r):
        if(arr[i] <= pivot):
            arr[i], arr[pIndex] = arr[pIndex], arr[i]
            pIndex += 1
    
    arr[pIndex], arr[r] = arr[r], arr[pIndex]
    return pIndex

arr = [1,6,2,5,3,4]

qsort(arr)

print(arr)