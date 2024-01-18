def reverse_text(text):
    reversed_text = ""
    for char in reversed(text):
        reversed_text += char
    return reversed_text

text="Ilyosbek"
print(reverse_text(text))