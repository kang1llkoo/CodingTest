x = input()
count = 0

while len(x) > 1:
    count += 1
    y = 0
    for i in x:
        y += int(i)
    x = str(y)

print(count)

if int(x) % 3 == 0:
    print("YES")
else:
    print("NO")