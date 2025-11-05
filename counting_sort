def counting_sort(a, k=None):
    if not a:
        return []
    if k is None:
        k = max(a)

    count = [0] * (k + 1)
    for x in a:
        count[x] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    out = [0] * len(a)
    for x in reversed(a):
        count[x] -= 1
        out[count[x]] = x

    return out


a = [4, 2, 2, 8, 3, 3, 1]
posortowany = counting_sort(a)   # => [1, 2, 2, 3, 3, 4, 8]
print(posortowany)
