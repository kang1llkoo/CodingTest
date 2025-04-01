vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

while True:
    line = input().strip()
    if line == '#':
        break
    count = sum(1 for char in line if char in vowels)
    print(count)