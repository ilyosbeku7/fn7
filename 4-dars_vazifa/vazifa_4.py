def reorder_numbers(numbers):
    numbers.sort(reverse=True)

    numbers = [str(num) for num in numbers]

    numbers.sort(key=lambda x: x[::-1])

    
    numbers = [int(num) for num in numbers]

    return numbers
numbers = [423, 587, 309]
reordered_numbers = reorder_numbers(numbers)
print(reordered_numbers)