def selection_sort(array):
    n = len(array)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array


sorted_array = selection_sort([3, 4, 1, 2, 5, 8, 6, 9, 7])
print(sorted_array)
