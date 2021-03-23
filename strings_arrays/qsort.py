def quicksort_(arr, l, h):
    if l < h:
        p = partition(arr, l, h)
        quicksort_(arr, l, p-1)
        quicksort_(arr, p+1, h)

def partition(arr, l, h):
    pivot = arr[h]
    i = l

    for j in range(l, h+1):
        if arr[j] < pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    arr[i], arr[h] = arr[h], arr[i]
    return i

def quicksort(arr):
    quicksort_(arr, 0, len(arr)-1)

if __name__ == '__main__':
    arr = [1,0,2,9,3,8,4,7,5,6]
    quicksort(arr)
    print(arr)