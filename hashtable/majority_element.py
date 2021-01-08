def majorityElement(arr, result):
    m = {}

    for i in arr:
        m[i] = m.get(i, 0) + 1
    
    for i in m:
        if m[i] > len(arr)/2:
            result.append(i)
    

result = []
majorityElement([1,1,2], result)
print(result)