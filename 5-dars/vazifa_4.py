def yetishmayotgan_raqam(nums):
    n=len(nums)+1
    expected_num=n*(n+1)//2
    actual_num=sum(nums)
    missing_num=expected_num-actual_num
    return missing_num

a=[0,2,3,1]
print(yetishmayotgan_raqam(a))