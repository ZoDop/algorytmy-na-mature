def prime(n):
    if n < 2:
        return False
    sqrt = int(n ** 0.5)
    for i in range(2, sqrt + 1):
        if n % i == 0:
            return False
    return True


def factors_all(n):
    i = 2
    while n > 1:
        if prime(i) and n % i == 0:
            n = n // i
            print(i, end=' ')
        else:
            i += 1


factors_all(120)
