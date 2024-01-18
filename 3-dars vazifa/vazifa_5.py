def find_index(lst, element):
    for i in range(len(lst)):
        if lst[i] == element:
            return i
    return "elememt topilmadi" 
my_list = [5, 2, 8, 1, 9]
element = 3
index = find_index(my_list, element)
print(index)  

