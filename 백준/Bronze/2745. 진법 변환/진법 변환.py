n, b = input().split()
b = int(b)

answer = 0
for i, char in enumerate(reversed(n)):
    if '0' <= char <= '9':
        digit = int(char)
    else:
        digit = ord(char) - ord('A') + 10
    
    answer += digit * (b**i)

print(answer)