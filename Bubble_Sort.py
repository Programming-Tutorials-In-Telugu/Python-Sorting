def bubble_sort(arr1):
    n = len(arr1)
    for i in range(n):
        for j in range(n - i - 1):
            if arr1[j] > arr1[j + 1]:
                arr1[j], arr1[j + 1] = arr1[j + 1], arr1[j]
    return arr1


sorted_array = bubble_sort([3, 4, 1, 2, 5, 6, 7, 10, 9, 8])
print(sorted_array)
