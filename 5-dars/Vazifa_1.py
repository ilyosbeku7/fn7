def duplikat(lst):
    unique = []
    duplicate_num = []
    for num in lst:
        if num not in unique:
            unique.append(num)
        else:
            duplicate_num.append('_')
    unique.extend(duplicate_num)
    return unique
a=[5, 2, 8, 5, 9, 4, 5, 9, 2]
print(duplikat(a))