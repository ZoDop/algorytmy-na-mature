def bucket_sort(arr):
    n = len(arr)
    if n == 0:
        return arr

    buckets = [[] for _ in range(n)]

    for x in arr:
        index = int(x * n)
        if index == n:
            index = n - 1
        buckets[index].append(x)

    for b in buckets:
        b.sort()

    result = []
    for b in buckets:
        result.extend(b)

    return result


nums = [0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51]
print("Przed sortowaniem:", nums)
sorted_nums = bucket_sort(nums)
print("Po sortowaniu    :", sorted_nums)
