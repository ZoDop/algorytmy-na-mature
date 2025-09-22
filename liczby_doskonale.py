numbers = [i for i in range(0, 100)]
def is_perfect(n):
    sum = 0
    i = 1
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n

print(is_perfect(1))


#sito erystotelesa

for i in range (2, 100):
    if numbers[i] != 0:
        print(numbers[i], end=" ")
        for w in range(2, 100):
            if i * w >= 100:
                break
            numbers[i * w] = 0