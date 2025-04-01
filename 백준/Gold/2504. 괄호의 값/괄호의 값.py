expression = input().strip()
stack = []
temp = 1
result = 0

for i in range(len(expression)):
    char = expression[i]

    if char == '(':
        stack.append(char)
        temp *= 2
    elif char == '[':
        stack.append(char)
        temp *= 3
    elif char == ')':
        if not stack or stack[-1] != '(':
            result = 0
            break
        if expression[i - 1] == '(':
            result += temp
        stack.pop()
        temp //= 2
    elif char == ']':
        if not stack or stack[-1] != '[':
            result = 0
            break
        if expression[i - 1] == '[':
            result += temp
        stack.pop()
        temp //= 3

print(result if not stack else 0)
