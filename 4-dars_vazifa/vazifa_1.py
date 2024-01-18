def sort_numbers(numbers):
    sorted_list = []

    while numbers:
        minimum = numbers[0] 
        for num in numbers:
            if num < minimum:
                minimum = num

        sorted_list.append(minimum)
        numbers.remove(minimum)

    return sorted_list

print(sort_numbers([2,9,4,15,36,12]))