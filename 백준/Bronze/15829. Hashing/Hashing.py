from string import ascii_lowercase

alpha_dict = {char: idx for idx, char in enumerate(ascii_lowercase, start=1)}

n = int(input())
input_str = input()
r = 31
M = 1234567891
result = 0
power = 1

for i in range(n):
    char = input_str[i]
    value = alpha_dict[char]
    result = (result + value * power) % M
    power = (power * r) % M

print(result)