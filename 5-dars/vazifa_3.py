def uniqu_num(nums):
    count=0
    left=0
    right=len(nums)-1
    while left<right:
        count+=1
        mid=(left+right)//2
       
        if mid %2 ==0:
            if nums[mid]==nums[mid+1]:
               left=mid+2
            else:
               right=mid
        else:
            if nums[mid]==nums[mid-1]:
                left=mid+1
            else:
                right=mid-1 
    return nums[left], count
a=[ 8, 8, 1, 9, 9, 4, 4, 5,5]
print(uniqu_num(a))