import sys

n = int(sys.stdin.readline().strip())
seq = [int(sys.stdin.readline().strip()) for _ in range(n)]

stack = []
result = []
curr = 1

for num in seq:
    while curr <= num:
        stack.append(curr)
        result.append("+")
        curr += 1

    if stack[-1] == num:
        stack.pop()
        result.append("-")
    else:
        print("NO")
        sys.exit()

sys.stdout.write("\n".join(result) + "\n")