
def to_octal(n: int) -> str:
    result = ""
    while n > 0:
        result = str(n % 8) + result
        n //= 8
    return result

print(to_octal(123))
#albo
print(oct(123)[2:])

def to_hex(n: int) -> str:
    digits = "0123456789abcdef"
    result = ""
    while n > 0:
        result = digits[n % 16] + result
        n //= 16
    return result

print(to_hex(123))
# albo
print(hex(123)[2:])
