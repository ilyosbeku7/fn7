def find_most_repeated(text):
    char_count = {}
    
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
   
    most_repeated = None
    max_count = 0
    
    for char, count in char_count.items():
        if count > max_count:
            most_repeated = char
            max_count = count
    
    return most_repeated

text='asdcvsxvagdfadfaaadwqqa'
print(find_most_repeated(text))