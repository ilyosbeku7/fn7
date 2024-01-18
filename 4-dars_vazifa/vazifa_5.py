import random

def raqamni_top(guess):
    random_number = random.randint(1, 50)
    low = 1
    high = 50

    while low <= high:
        mid = (low + high) // 2

        if guess == mid:
            return "tabriklaymiz! siz to'g'ri javobni topdingiz."
        elif guess < mid:
            high = mid - 1
            print ("javob noto'g'ri. kattaroq raqamni sinab ko'rin")
        else:
            low = mid + 1
            print ("javob noto'g'ri. kichikroq raqamni sinab ko'rin")

    return guess


foydalanuvchi = 26
result = raqamni_top(foydalanuvchi)
print(result)