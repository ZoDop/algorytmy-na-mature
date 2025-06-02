
def anagram1(w1, w2):
    l1 = {}
    l2 = {}
    for i in w1:
        if i not in l1:
            l1[i] = 0
        l1[i] += 1
    for i in w2:
        if i not in l2:
            l2[i] = 0
        l2[i] += 1
    return l1 == l2

def anagram2(w1, w2):
    counts = [0] * 10
    for i in w1:
        counts[int(i)] += 1
    for i in w2:
        counts[int(i)] -= 1
    for count in counts:
        if count != 0:
            return False
    return True

def anagram3(w1, w2):
    return sorted(w1) == sorted(w2)



file = open("podciagi_anagram.txt", "r")
numbers = []
for line in file:
    numbers.append(line.strip())

n = len(numbers)
max_length = 0
max_index = 0
first = 0
lenght = 0
index = 0

for first in range(1, n):
    if anagram2(numbers[first], numbers[first - 1]) and lenght == 0:
        lenght = 2
        index = first
    elif anagram2(numbers[first], numbers[first - 1]) and lenght > 0:
        lenght += 1
        if lenght > max_length:
            max_length = lenght
            max_index = index
    else:
        lenght = 1


print(max_index, max_length)