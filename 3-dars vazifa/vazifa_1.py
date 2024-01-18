def add_lists(list1, list2):
    result = []
    length = min(len(list1), len(list2))  
    
    for i in range(length):
        sum_of_elements = list1[i] + list2[i]
        result.append(sum_of_elements)
    
    return result
list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40, 50]

result = add_lists(list2, list1)
print(result)  