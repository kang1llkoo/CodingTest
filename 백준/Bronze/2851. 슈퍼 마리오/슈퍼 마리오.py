mushroom = [int(input()) for _ in range(10)]

total = 0
for i in range(10):
    total += mushroom[i]
    if total >= 100:
        if abs(total - 100) <= abs(total - mushroom[i] - 100):
            print(total)
        else:
            print(total - mushroom[i])
        break
else:
    print(total)