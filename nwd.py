import math
def gcd(a, b):
    if a == b:
        return a
    if a > b:
        return gcd(a - b, b)
    return gcd(b - a, a)

print(gcd(10, 5))

def nwd(a, b):
    while b:
        a, b = b, a % b
    return a

print(nwd(10, 15))

print(math.gcd(5, 10))
