def maxSum(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    n = len(arr)

    for i in range(0, n-k):
        window_sum = window_sum + arr[i+2] - arr[i]
        max_sum = max(window_sum, max_sum)
    
    return max_sum

print(maxSum([1,2,3,4,5,6,7,8,9], 2))