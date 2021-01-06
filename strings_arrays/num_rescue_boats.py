def numBoats(arr, limit):
    arr.sort()
    i = 0; j = len(arr) - 1
    num_boats = 0

    while(i <= j):
        if(i == j):
            num_boats += 1
            i += 1
        else:
            if arr[i] + arr[j] <= limit:
                num_boats += 1
                i += 1
            else:
                num_boats += 1
        
        j -= 1
    
    return num_boats

print(numBoats([3,2,2,1], 3))