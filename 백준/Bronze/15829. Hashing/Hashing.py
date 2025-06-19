from string import ascii_lowercase

alpha_dict = {char: idx for idx, char in enumerate(ascii_lowercase, start = 1)}

n = int(input())
str = input()
m = 31
result = 0

for i in range(n):
    char = str[i]
    value = alpha_dict[char]
    result += value * (m**i)

print(result)