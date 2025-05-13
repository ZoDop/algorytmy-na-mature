
# dla wszystkich do dziesiętnego
def from_bin(n: str) -> int:
    sum = 0
    exp = len(n) - 1
    for i in range(len(n)):
        sum += int(n[i]) * 2 ** exp
        exp -= 1
    return sum

print(from_bin("101010"))
#albo
print(int("101010", 2))


# od dziesiętnego w góre
def from_hex(n: str) -> int:
    sum = 0
    exp = len(n) - 1
    for i in range(len(n)):
        if ord(hex[i]) >= 97:
            sum += (ord(n[i]) - 97 + 10) * 16 ** exp
        else:
            sum += (ord(n[i]) - 48) * 16 ** exp
        exp -= 1
    return sum