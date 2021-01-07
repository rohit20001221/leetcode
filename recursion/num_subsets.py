def subSets(arr):
    ans = []
    current = []
    getSubSets(arr, current, 0, ans)
    return ans

def getSubSets(arr, current, index, ans):
    if index >= len(arr):
        return
    
    ans.append(current[:])

    for i in range(index, len(arr)):
        if (arr[i] not in current):
            current.append(arr[i])
            getSubSets(arr, current, i, ans)
            current.pop()

print(subSets([1,2,3]))