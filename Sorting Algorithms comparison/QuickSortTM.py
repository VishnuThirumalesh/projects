def mid_val(arr, leftend, rightend):
    left = arr[leftend]
    right = arr[rightend-1]
    length = rightend - leftend
    if length % 2 == 0:
        middle = arr[leftend + int(length/2) - 1]
    else:
        middle = arr[leftend + int(length/2)]
  
    pivot = median(left, right, middle)

    pivotindex = arr.index(pivot) 
    arr[pivotindex] = arr[leftend]
    arr[leftend] = pivot

    i = leftend + 1
    for j in range(leftend + 1, rightend):
        if arr[j] < pivot:
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
            i += 1

    leftendval = arr[leftend]
    arr[leftend] = arr[i-1]
    arr[i-1] = leftendval
    return i - 1


def median(a, b, c):
    if ( a - b) * (c - a) >= 0:
        return a
    elif (b - a) * (c - b) >= 0:
        return b
    else:
        return c


def QuickSort(arr, low, high):
     if low < high:
         mid = mid_val(arr, low, high)
         QuickSort(arr, low, mid)
         QuickSort(arr, mid + 1, high)
     return arr
