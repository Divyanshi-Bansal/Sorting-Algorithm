def bubble_sort(numbers):
    l = len(numbers)
    for i in range(l):
        for j in range(l - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]


numbers = [9, 59, 41, 34, 5, 61, 7, 1]
print("Before Sorting", numbers)
bubble_sort(numbers)
print("After Sorting", numbers)
