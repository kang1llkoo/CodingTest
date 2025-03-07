word = input()
pre = ['a', 'e', 'i', 'o', 'u']
count = 0
for char in pre:
    count += word.count(char)

print(count)