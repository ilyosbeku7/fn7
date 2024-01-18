def is_number_palindrome(number):
    
    number_str = str(number)
        
    return number_str == number_str[::-1]

num=12321
num2=12345
print(is_number_palindrome(num2))