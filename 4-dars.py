# d=25

# def my_fun():
#     prefix="Salom"
#     print(f"{prefix} is {d}")

# my_fun()

# def outer ():
#     a=25
#     name="python"
#     def inner (prefiix):
#         print (f"{name} is {prefiix}")
#     return inner

# my_list = [1,2,3,4,5,6,7,8,9]   #linear search- 9 marta 

my_list2 = [1,2,3,4,5,6,7,8,9,10]

def bimary_search(my_list, target):
    end=len(my_list)-1
    start=0
    count=0
    while start<=end:
        mid_index=(start+end)//2
        mid_value=my_list[mid_index]
        count=count+1

        if mid_value==target:
            return f"{target} sonning list ichidegi indexi {mid_index} va urinishlar soni {count}ta"
        elif mid_value>target:
            end=mid_index-1
        else:
            start=mid_index+1
        
print (bimary_search(my_list2, 5))

