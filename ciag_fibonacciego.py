
def fibonacci_rekurencja(n):
    if n ==0:
        return 0
    if n == 1:
        return 1
    return fibonacci_rekurencja(n - 1) + fibonacci_rekurencja(n - 2)

print(fibonacci_rekurencja(10))


list = [0] * 10000
list[1] = 1
def fibonacci_rekurencja_memoization(n, list):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if list[n] != 0:
        return list[n]
    list[n] = fibonacci_rekurencja_memoization(n - 1, list) + fibonacci_rekurencja_memoization(n - 2, list)
    return list[n]

print(fibonacci_rekurencja_memoization(10, list))


def fibonacci_petla(n):
    list = [0, 1, 1]
    while len(list) <= n:
        list.append(list[-1] + list[-2])
    return list[-1]

print(fibonacci_petla(10))