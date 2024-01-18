my_list = [5, 2, 8, 1, 9]

def insertion_sort(list_a):
    lenght=len(list_a)

    count=0
    for i in range(1, lenght):

        while list_a[i]<list_a[i-1] and i>0:
            count=count+1
            list_a[i], list_a[i-1]= list_a[i-1], list_a[i]
            i=i-1
        
    return  list_a

print(insertion_sort(my_list))
