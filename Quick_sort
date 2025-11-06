def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # bierzemy środkowy element jako pivot

    left  = [x for x in arr if x < pivot]
    mid   = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + mid + quicksort(right)


nums = [5, 3, 8, 4, 2, 7, 1, 10]
print(quicksort(nums))  # [1, 2, 3, 4, 5, 7, 8, 10]
