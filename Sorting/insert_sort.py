def insert_sort(arr):
    for i in range(1, len(arr)):
        marker = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > marker:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = marker

    return arr

print(insert_sort([5, 2, 4, 3, 2, 1]))