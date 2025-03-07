n = input()
middle = len(n) // 2
left = list(n[:middle])
right = list(n[middle:])
sum_left = sum(int(n) for n in left)
sum_right = sum(int(n) for n in right)
if sum_left == sum_right:
    print("LUCKY")
else:
    print("READY")