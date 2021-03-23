def quicksort_(arr, l, h):
    if l < h:
        p = partition(arr, l, h, scheme='l')
        quicksort_(arr, l, p-1)
        quicksort_(arr, p+1, h)

def partition(arr, l, h, scheme='l'):
    if scheme == 'l':
        pivot = arr[h]
        i = l

        for j in range(l, h+1):
            if arr[j] < pivot:
                arr[j], arr[i] = arr[i], arr[j]
                i += 1
        arr[i], arr[h] = arr[h], arr[i]
        return i
    else:
        pivot = arr[(l+h)//2]

        i = l-1
        j = h+1

        while True:
            i += 1
            while arr[i] < pivot:
                i += 1
            j -= 1
            while arr[j] > pivot:
                j -= 1
            if i >= j:
                return j
            
            arr[i], arr[j] = arr[j], arr[i]
            

def quicksort(arr):
    quicksort_(arr, 0, len(arr)-1)

if __name__ == '__main__':
    arr = [1,0,2,9,3,8,14,12,5,6]
    quicksort(arr)
    print(arr)