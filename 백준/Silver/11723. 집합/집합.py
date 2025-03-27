import sys

input = sys.stdin.readline
n = int(sys.stdin.readline())
arr = set()
for _ in range(n):
    command = input().strip().split()
    if command[0] == "add":
        arr.add(int(command[1]))
    elif command[0] == "remove":
        arr.discard(int(command[1]))
    elif command[0] == "check":
        print(1 if int(command[1]) in arr else 0)
    elif command[0] == "toggle":
        x = int(command[1])
        if x in arr:
            arr.discard(x)
        else:
            arr.add(x)
    elif command[0] == "all":
        arr = set(range(1, 21))
    elif command[0] == "empty":
        arr.clear()