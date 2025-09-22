
numbers = [2, 3, 4, 6, 5, 8, 7, 9]

def selection_sort(numbers):
    n = len(numbers)
    for first in range(n):
        min = first
        for i in range(first + 1, n):
            if numbers[i] > numbers[min]:
                min = i
        temp = numbers[min]
        numbers[min] = numbers[first]
        numbers[first] = temp

selection_sort(numbers)
print(numbers)

