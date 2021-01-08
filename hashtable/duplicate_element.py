def containsDuplicate(arr):
    m = {}

    for i in arr:
        if i in m:
            return True
        
        m[i] = 1
    
    return False

print(containsDuplicate([1,2,3,4]))
print(containsDuplicate([1,9,4,2,3,1]))