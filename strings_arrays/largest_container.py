def largeContainer(arr):
    maxarea = 0
    l = 0
    r = len(arr) - 1

    while(l < r):
        maxarea = max(maxarea, min(arr[l], arr[r])*(r-l))

        if arr[r] < arr[l]:
            r -= 1
        else:
            l += 1
    
    return maxarea

print(largeContainer([1,8,6,2,5,4,8,3,7]))