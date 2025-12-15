def rozklad_na_czynniki(n):
    czynniki = set()
    i = 2
    while i * i <= n:
        while n % i == 0:
            czynniki.add(i)
            n //= i
        i += 1
    if n > 1:
        czynniki.add(n)
    return czynniki
