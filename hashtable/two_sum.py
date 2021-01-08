def twoSum(arr, target):
    m = {}
    for i in range(len(arr)):
        goal = target - arr[i]
        if goal in m:
            return (i, m[goal])
        
        if arr[i] not in m:
            m[arr[i]] = i
    
    return

print(twoSum([3,2,1,5], 8))