def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    left = []
    right = []

    for i in range(len(arr)):
        if i < len(arr)/2:
            left.append(arr[i])
        else:
            right.append(arr[i])
    
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(arr1, arr2):
    result = []

    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    
    while i < len(arr1):
        result.append(arr1[i])
        i += 1
    
    while j < len(arr2):
        result.append(arr2[j])
        j += 1
    
    return result



print(merge_sort([1,9,2,8,3,7,4,6,5]))