s = input()

alpha = [0] * 26

for char in s:
    alpha[ord(char) - ord('a')] += 1

print(*alpha)