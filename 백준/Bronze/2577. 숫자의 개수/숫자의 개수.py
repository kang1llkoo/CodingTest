a = int(input())
b = int(input())
c = int(input())

target = a*b*c
count = {str(i):0 for i in range(0,10)}

for char in str(target):
    if char in count:
        count[char] += 1

for i in range(10):
    print(count[str(i)])