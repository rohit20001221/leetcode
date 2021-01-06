def firstIndex(arr, k):
    l = 0; r = len(arr) - 1
    # mid = (l+r) // 2
    
    while(l <= r):
        mid = (l+r) // 2
        if(arr[mid] == k):
            if (mid == 0 or arr[mid-1] != k):
                return mid
            r = mid - 1
        elif(k < arr[mid]):
            r = mid - 1
        else:
            l = mid + 1
    
    return mid

def lastIndex(arr, k):
    l = 0; r = len(arr) - 1

    while(l <= r):
        mid = (l+r) // 2

        if(arr[mid] == k):
            if(mid == len(arr)-1 or arr[mid+1] != k):
                return mid
            l = mid + 1
        elif(k < arr[mid]):
            r = mid - 1
        else:
            l = mid + 1
    return mid

print(firstIndex([1,11,11,11,12,14,15,15,15,17,18], 15))
print(lastIndex([1,11,11,11,12,14,15,15,15,17,18], 15))