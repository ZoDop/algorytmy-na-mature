
numbers = [2, 3, 4, 6, 5, 8, 7, 9]

def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n):
        for k in range(n - 1 - i):
            if numbers[k] < numbers[k + 1]:
                numbers[k], numbers[k + 1] = numbers[k + 1], numbers[k]

bubble_sort(numbers)
print(numbers)