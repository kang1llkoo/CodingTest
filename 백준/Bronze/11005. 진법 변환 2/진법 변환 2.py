n, b = map(int, input().split())

digits = []
while n > 0:
    remain = n % b
    if remain < 10:
        digits.append(str(remain))
    else:
        digits.append(chr(remain - 10 + ord('A')))
    n //= b

print(''.join(digits[::-1]))