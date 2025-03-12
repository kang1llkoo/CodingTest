n = int(input())
original = n
count = 0

while True:
    ten = n // 10
    one = n % 10
    new = (ten + one) % 10
    n = one * 10 + new
    count += 1

    if n == original:
        break

print(count)