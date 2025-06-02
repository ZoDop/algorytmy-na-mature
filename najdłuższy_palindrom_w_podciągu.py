
def pallindrome(s: str) -> bool:
    return s == s[::-1]


file = open("podciagi_palindrom.txt", "r")
numbers = []
for line in file:
    numbers.append(line.strip())

n = len(numbers)
max_length = 0
max_index = 0

for first in range(n):
    if pallindrome(numbers[first]):
        lenght = 1
        for last in range(first + 1, n):
            if pallindrome(numbers[last]):
                lenght += 1
                if lenght > max_length:
                    max_length = lenght
                    max_index = first
            else:
                break

print(max_index + 1, max_length)


# lepszy sposób


def pallindrome(s: str) -> bool:
    return s == s[::-1]


file = open("podciagi_palindrom.txt", "r")
numbers = []
for line in file:
    numbers.append(line.strip())

n = len(numbers)
max_length = 0
max_index = 0
first = 0
lenght = 0
index = 0

for first in range(n):
    if pallindrome(numbers[first]) and lenght == 0:
        lenght = 1
        index = first
    elif pallindrome(numbers[first]) and lenght > 0:
        lenght += 1
        if lenght > max_length:
            max_length = lenght
            max_index = index
    else:
        lenght = 0


print(max_index + 1, max_length)