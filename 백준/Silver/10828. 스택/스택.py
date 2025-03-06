import sys

n = int(sys.stdin.readline().strip())
stack = []
result = []

for _ in range(n):
    command = sys.stdin.readline().strip().split()

    if command[0] == "push":
        stack.append(int(command[1]))
    elif command[0] == "pop":
        result.append(str(stack.pop()) if stack else "-1")
    elif command[0] == "size":
        result.append(str(len(stack)))
    elif command[0] == "empty":
        result.append("1" if not stack else "0")
    elif command[0] == "top":
        result.append(str(stack[-1]) if stack else "-1")

sys.stdout.write("\n".join(result)+"\n")