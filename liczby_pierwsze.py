def prime(n):
    int(n)
    if n < 2:
        return False
    sqrt = n ** 0.5
    for i in range(2, int(sqrt) + 1):
        if n % i == 0:
            return False
    return True


prime(5)

