def sort(t):
    n = len(t)
    if n <= 1:
        return t[:]

    sr = n // 2
    lewo = sort(t[:sr])
    prawo = sort(t[sr:])

    i = j = 0
    c = []
    while i < len(lewo) and j < len(prawo):
        if lewo[i] <= prawo[j]:
            c.append(lewo[i])
            i += 1
        else:
            c.append(prawo[j])
            j += 1

    while i < len(lewo):
        c.append(lewo[i])
        i += 1
    while j < len(prawo):
        c.append(prawo[j])
        j += 1

    return c


a = [5, 2, 4, 6, 1, 3]
print(sort(a))  # [1, 2, 3, 4, 5, 6]
