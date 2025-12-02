def bubbleSort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1): 
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
data = [14, 46, 43, 27, 57, 41, 45, 21, 70]
print("Mảng ban đầu:", data)
print("Mảng sau khi sắp xếp:", bubbleSort(data))
