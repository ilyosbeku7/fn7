def check_brackets(text):
    stack = []

    for char in text:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if len(stack) == 0 or stack[-1] != '(':
                return False
            stack.pop()

    return len(stack) == 0

a="((2+2)+4*5)=24"
print(check_brackets(a))