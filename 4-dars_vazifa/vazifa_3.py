def count_words(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        print("File not found.")
        return 0


filename = 'text.txt'
word_count = count_words(filename)
print("Number of words:", word_count)


